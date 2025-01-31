from langchain_community.document_loaders.generic import GenericLoader 
from langchain_community.document_loaders.parsers import LanguageParser

# Importações para processamento e segmentação do código
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

# Importações para criação das cadeias de processamento de perguntas e respostas
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

import os
from git import Repo

os.environ["OPENAI_API_KEY"] = ""
repo_path = "./test_repo"


if not os.path.exists(os.path.join(repo_path, ".git")):
    repo = Repo.clone_from("https://github.com/welingtoncassis/llms-rag", to_path=repo_path)
    print("Repositório clonado com sucesso.")
else:
    repo = Repo(repo_path)
    print("Repositório já existe, ignorando clonagem.")

# Configuração do loader para carregar arquivos de código Python do repositório
# O código será carregado a partir do diretório 'rag-pdf-document/', excluindo arquivos com codificação não UTF-8
loader = GenericLoader.from_filesystem(
    repo_path + "/rag-pdf-document/", 
    glob = "**/*", # Carregar todos os arquivos recursivamente
    suffixes = [".py"], # Filtrar apenas arquivos Python
    exclude = ["**/non-utf-8-encoding.py"], # Excluir arquivos problemáticos
    parser = LanguageParser(language=Language.PYTHON, parser_threshold = 500) # Parser para processar os arquivos
)
documents = loader.load()

# Dividir o código carregado em pequenos blocos (chunks) para facilitar o processamento
python_splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON, 
    chunk_size = 500, # Tamanho de cada segmento de código
    chunk_overlap = 50 # Sobreposição entre os segmentos para manter o contexto
)
texts = python_splitter.split_documents(documents)

# Criar um banco de dados vetorial para armazenar os chunks de código
# Os embeddings são gerados para permitir a recuperação eficiente de informações
# utilizando OpenAIEmbeddings.
db = Chroma.from_documents(texts, OpenAIEmbeddings(disallowed_special=()))

# Configurar o mecanismo de recuperação de informações com busca baseada em MMR (Maximal Marginal Relevance)
retriver = db.as_retriever(
    search_type = "mmr", # Prioriza diversidade nos resultados recuperados
    search_kwargs = {"k":8} # Número de resultados retornados por busca
)

# Configurar o modelo de linguagem para análise e revisão de código
llm = ChatOpenAI(model="gpt-3.5-turbo", max_tokens=250)

# Criar o prompt que será utilizado para interagir com o modelo de IA
# Ele fornece um contexto detalhado para revisão de código e sugestões de melhoria
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Você é um revisor de código experiente, Forneça informações etalhadas sobre a revisão do código e sugestões de melhorias baseado no contexto fornecido abaixo: \n\n {context}"
        ),
        (
            "user", "{input}"
        )
    ]
)

document_chain = create_stuff_documents_chain(llm, prompt)
retieval_chain = create_retrieval_chain(retriver, document_chain)

# Realizar a análise do código com base na pergunta fornecida
response = retieval_chain.invoke({"input": "Voce pode revisar o código e sugerir melhores no código do método ask?"})
print(response['answer'])
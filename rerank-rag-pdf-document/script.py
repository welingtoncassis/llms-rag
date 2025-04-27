# Carregando variáveis de ambiente do .env
from dotenv import load_dotenv
load_dotenv()

# Importações
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_cohere import CohereRerank

# LISTANDO AS PERGUNTAS A SEREM RESPONDIDAS
questions = [
    "Qual é a visão de Euclides da Cunha sobre o ambiente natural do sertão nordestino e como ele influencia a vida dos habitantes?",
    "Quais são as principais características da população sertaneja descritas por Euclides da Cunha? Como ele relaciona essas características com o ambiente em que vivem?",
    "Qual foi o contexto histórico e político que levou à Guerra de Canudos, segundo Euclides da Cunha?",
    "Como Euclides da Cunha descreve a figura de Antônio Conselheiro e seu papel na Guerra de Canudos?",
    "Quais são os principais aspectos da crítica social e política presentes em \"Os Sertões\"? Como esses aspectos refletem a visão do autor sobre o Brasil da época?",
]

# Carregando os modelos OpenAI - Embedding e Chat
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    max_tokens=500,
)

# Carregando o PDF
pdf_link = "os-sertoes.pdf"
loader = PyPDFLoader(pdf_link, extract_images=False)
pages = loader.load_and_split()

# Separando o conteúdo em chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=4000,
    chunk_overlap=20,
    length_function=len,
    add_start_index=True,
)
chunks = text_splitter.split_documents(pages)

# Salvando os chunks no VectorDB
vectordb = Chroma(embedding_function=embeddings)
vectordb.add_documents(chunks)

# Configurando o recuperador
naive_retriever = vectordb.as_retriever(search_kwargs={"k": 10})

# Configurando o Reranker
rerank = CohereRerank(model="rerank-v3.5", top_n=3)

# Criando o ContextualCompressionRetriever
compressor_retriever = ContextualCompressionRetriever(
    base_compressor=rerank,
    base_retriever=naive_retriever,
)

# Definindo o template para o prompt de Chat
TEMPLATE = """
Você é um especialista em literatura brasileira. Responda a pergunta abaixo utilizando o contexto informado

Contexto: {context}
    
Pergunta: {question}
"""

rag_prompt = ChatPromptTemplate.from_template(TEMPLATE)

# Configurando o processo de recuperação paralelo
setup_retrieval = RunnableParallel({
    "question": RunnablePassthrough(),
    "context": compressor_retriever
})

output_parser = StrOutputParser()

# Criando a cadeia de recuperação com compressão
compressor_retrieval_chain = setup_retrieval | rag_prompt | llm | output_parser

# Função para responder uma pergunta
def answer_question(question: str) -> str:
    return compressor_retrieval_chain.invoke(question)

# Executando as perguntas (Exemplo de uso)
if __name__ == "__main__":
    for idx, question in enumerate(questions):
        resposta = answer_question(question)
        print({
            "numero": idx,
            "pergunta": question,
            "resposta": resposta,
        })

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.document_loaders import PyMuPDFLoader
from langchain.chains.question_answering import load_qa_chain

import os

os.environ["OPENAI_API_KEY"] = "yourkey"

#load dos modelos que serao usados (embeddings e LLM)
embeddings_model = OpenAIEmbeddings()
llm = ChatOpenAI(model_name = "gpt-3.5-turbo", max_tokens = 200)

#Carregar o pdf
pdf_link = "os-sertoes.pdf"
loader = PyMuPDFLoader(pdf_link)
documents = loader.load()

#Separar em chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 4000,
    chunk_overlap = 20,
    length_function = len,
    add_start_index = True,
)
chunks = text_splitter.split_documents(documents)

#Salvar no vector db - chroma
db = Chroma.from_documents(chunks, embedding=embeddings_model, persist_directory="text_index")

#Carregar DB
vectordb = Chroma(persist_directory="text_index", embedding_function=embeddings_model)

#Load Retriever
retriever = vectordb.as_retriever(search_kwargs={"k":3}) #Vai procurar os 3 arquivos/chunks mais relevantes

#Construcao da cadeia de prompt para a chamada do LLM
chain = load_qa_chain(llm,chain_type="stuff")

def ask(question):
    context = retriever.get_relevant_documents(question) # Recupera os chunks relevantes a question
    answer = (chain({"input_documents": context, "question": question}, return_only_outputs=True))['output_text']
    return answer

user_question = input("User: ")
answer = ask(user_question)
print("Answer: ", answer)
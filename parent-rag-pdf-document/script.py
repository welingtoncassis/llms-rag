from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", max_tokens=300)

pdf_link = "os-sertoes.pdf"

loader = PyPDFLoader(pdf_link, extract_images=False)
pages = loader.load_and_split()


child_splitter = RecursiveCharacterTextSplitter(chunk_size = 200)
parent_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 200,
    length_function = len,
    add_start_index = True
)

store = InMemoryStore()
vectorstore = Chroma(embedding_function=embeddings, persist_directory='childVectorDB')

parent_document_retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=store,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter
)

parent_document_retriever.add_documents(pages, ids=None)

parent_document_retriever.vectorstore.get()

TEMPLATE =  """
    Você é um especialista em literatura brasileira. Responda a pergunta abaixo utilizando o contexto informado
    Query:
    {question}

    Context:
    {context}
"""
rag_prompt = ChatPromptTemplate.from_template(TEMPLATE)

setup_retrival = RunnableParallel({"question": RunnablePassthrough(), "contect": parent_document_retriever})
output_parser = StrOutputParser()

parent_chain_retrival = setup_retrival | rag_prompt | llm | output_parser

parent_chain_retrival.invoke("Quais as tecnologias usadas pelo candidato?")

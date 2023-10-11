import os 
from langchain import HuggingFaceHub, PromptTemplate, LLMChain
from langchain.vectorstores import Milvus

from langchain.document_loaders import DirectoryLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
import pinecone 
from langchain.vectorstores import Pinecone


def load_docs(directory):
  loader = DirectoryLoader(directory)
  documents = loader.load()
  return documents

def split_docs(documents,chunk_size=500,chunk_overlap=20):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs


def main():

  directory = 'data/documents/legal'

  documents = load_docs(directory)

  docs = split_docs(documents)

  embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")


  pinecone.init(
      api_key=os.getenv("PINECONE_API_TOKEN"),  
      environment="gcp-starter")
  
  index_name = "langchain-tryout"
  index = Pinecone.from_documents(docs, embeddings, index_name=index_name)



if __name__ == "__main__":
  main()




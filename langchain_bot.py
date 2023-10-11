import os 

from langchain.chains import RetrievalQA

from langchain.vectorstores import Pinecone
import pinecone

pinecone.init(
    api_key=os.getenv("PINECONE_API_TOKEN"),  
    environment="gcp-starter"
)

def execute_query(query, 
                  embedd, 
                  model):

    index_name = "langchain-tryout"
    docsearch = Pinecone.from_existing_index(index_name, embedd)
    qa = RetrievalQA.from_chain_type(llm=model, chain_type="stuff", retriever=docsearch.as_retriever())
    query_german = query + " Answer in German."
    return qa.run(query_german)



if __name__ == "__main__":
    pass
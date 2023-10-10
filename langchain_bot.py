import os 
from langchain import HuggingFaceHub, PromptTemplate, LLMChain

from langchain.chains import RetrievalQA
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Pinecone
import pinecone



def execute_query(query):

    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")


    model_id = "mistralai/Mistral-7B-Instruct-v0.1"
    conv_model = HuggingFaceHub(huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"), 
                                repo_id = model_id, 
                                model_kwargs={'temperature': 0.8, 'max_new_tokens': 200})


    pinecone.init(
        api_key=os.getenv("PINECONE_API_TOKEN"),  
        environment="gcp-starter"
    )

    index_name = "langchain-tryout"
    docsearch = Pinecone.from_existing_index(index_name, embeddings)
    qa = RetrievalQA.from_chain_type(llm=conv_model, chain_type="stuff", retriever=docsearch.as_retriever())
    #print(qa.run(query))
    query_german = query + " Antworte auf Deutsch."
    return qa.run(query_german)



if __name__ == "__main__":
    pass
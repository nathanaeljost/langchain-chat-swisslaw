# Open source document query AI chatbot (POC)

---

## Description

This project serves as proof of concept for a custom-knowledge chatbot using [LangChain](https://python.langchain.com/docs/get_started/introduction), [Huggingface](https://huggingface.co/), and [Pinecone](https://www.pinecone.io/). The custom knowledge in this project is comprised of the Swiss tenant law (found [here](https://www.mietrecht.ch/fileadmin/files/Gesetze/OR_mietrecht_A4.pdf)). For the LLM, [Mistral-7B-Instruct-v0.1](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) was used. 

`load_pinecone.py`: Splits the .txt files are split into chunks, creates embeddings for the sequences and subsequently loads into a vector database (Pinecone) via API.
<br>

`langchain_bot.py`: Initializes pinecone connection, executes a similarity search and subsequently generates answer via `RetrievalQA()` using the model provided. 
<br>

`tenant_law_app.py`: Initializes mistral model & embeddings (via `SentenceTransformerEmbeddings`) and creates a simple customtkinter application, which accepts a question input and displays the AI-generated output. 

## Example

![ScreenShot](/images/screenshot.png)

## Sources
* [Introduction to langchain](https://blog.devgenius.io/introduction-to-langchain-ef84eec62a65)
* [Chatbot with Langchain, ChatGPT, Pinecone, and Streamlit](https://blog.futuresmart.ai/building-an-interactive-chatbot-with-langchain-chatgpt-pinecone-and-streamlit)

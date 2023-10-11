import customtkinter

from tkinter import *
from pytube import *
from langchain_bot import *

from langchain import HuggingFaceHub
from langchain.embeddings import SentenceTransformerEmbeddings

embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

model_id = "mistralai/Mistral-7B-Instruct-v0.1"
conv_model = HuggingFaceHub(huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"), 
                            repo_id = model_id, 
                            model_kwargs={'temperature': 0.8, 'max_new_tokens': 200}) # adjust temperature for more or less deterministic / diverse outputs.


def generate_answer():
    textbox_a.delete("0.0", "end")
    question = textbox_q.get('1.0', END)
    answer = execute_query(question, embeddings, conv_model)
    textbox_a.insert("0.0",answer)


customtkinter.set_appearance_mode("dark") 
root = customtkinter.CTk()
root.geometry("600x400")
root.title("Chatbot Mietrecht")


# Question

header_1 = customtkinter.CTkLabel(root, text = "Stelle eine Frage zum Schweizer Mietrecht")
header_1.place(relx=0.5, rely=0.1, anchor=CENTER)

textbox_q = customtkinter.CTkTextbox(root, height=100, width=550)
textbox_q.place(relx=0.5, rely=0.3, anchor=CENTER)

# Answer

header_2 = customtkinter.CTkLabel(root, text = "KI-generierte Antwort:")
header_2.place(relx=0.5, rely=0.5, anchor=CENTER)

textbox_a = customtkinter.CTkTextbox(root, height=120, width=550)
textbox_a.place(relx=0.5, rely=0.7, anchor=CENTER)

button = customtkinter.CTkButton(root, command=generate_answer, text='Generieren')
button.place(relx=0.5, rely=0.9, anchor=CENTER)


root.mainloop()
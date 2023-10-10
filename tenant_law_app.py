from pytube import *
from tkinter import *
import customtkinter
import tkinter

from langchain_bot import *

customtkinter.set_appearance_mode("dark") 

def getText():
    textbox_a.delete("0.0", "end")
    question = textbox_q.get('1.0', END)
    answer = execute_query(question)
    textbox_a.insert("0.0",answer)


root = customtkinter.CTk()
root.geometry("600x400")
root.title("Chatbot Mietrecht")


# Question

header_1 = customtkinter.CTkLabel(root, text = "Stelle eine Frage zum Schweizer Mietrecht")
header_1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

textbox_q = customtkinter.CTkTextbox(root, height=100, width=550)
textbox_q.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

# Answer

header_2 = customtkinter.CTkLabel(root, text = "KI-generierte Antwort:")
header_2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

textbox_a = customtkinter.CTkTextbox(root, height=120, width=550)
textbox_a.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(root, command=getText, text='Generieren')
button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)


root.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
janela = tk.Tk()
janela.title("Sistema de login ")
janela.geometry("350x200")

def login():
    usuario = edt_login.get()
    senha = edt_senha.get()

    if usuario == "Jean" and senha == "123":
        messagebox("Login realizado com sucesso!")
    else: 
        messagebox.showerror("Erro", "usuário ou senha inválidos!")

lbl_login = ttk.Label(
    janela, 
    text="Login:"
)
lbl_login.grid(
    row=0, 
    colum=0,
    padx=10,
    pady=10
)
edt_login = ttk.Entry(
    janela,
    witdh=25
)
edt_login.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)

############################
lbl_senha = ttk.Label(
    janela, 
    text="Login:"
)
lbl_senha.grid(
    row=1, 
    colum=0,
    padx=10,
    pady=10
)
edt_senha = ttk.Entry(
    janela,
    witdh=25,
    show="*"
)
edt_senha.grid(
    row=1,
    column=1,
    padx=10,
    pady=10
)

janela.mainloop()





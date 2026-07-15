import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
janela = tk.Tk()
janela.title("Sistema de Login ")
janela.geometry("350x200")

def login():
    usuario = edt_login.get()
    senha = edt_senha.get()

    if usuario == "Fudencio" and senha == "123":
        messagebox.showinfo("Login","Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos!")

lbl_login = ttk.Label(
    janela,
    text="Login:"
)
lbl_login.grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)
edt_login = ttk.Entry(
    janela,
    width=25
)
edt_login.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)    

#########################
lbl_senha = ttk.Label(
    janela,
    text="Senha:"
)
lbl_senha.grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)
edt_senha = ttk.Entry(
    janela,
    width=25,
    show="*"
)
edt_senha.grid(
    row=1,
    column=1,
    padx=10,
    pady=10
)       

# Criar o botão de login
btn_login = ttk.Button(
    janela,
    text = "Entrar",
    command=login
)
btn_login.grid(
    row=2,
    column=0,
    columnspan=2
)
janela.mainloop()



import tkinter as tk
from tkinter import Label, Entry, Button, messagebox

def mostrar_mensagem():
    nome = txt_nome.get()
    if(nome.strip()):
        lbl_resultado['text'] = (f"Bem_vindo(a) {nome}")
        txt_nome.delete(0, tk.END)
        messagebox.showinfo("Acesso ao sistema", f"Bem_vindo(a) {nome}")
    else:
        messagebox.showerror("Error", f"Informe seu nome!!")

#1. Criar a janela
janela = tk.Tk()

#2. Configurar a janela
janela.title("Boas vindas ao sistema")
janela.geometry("300x400") #Tamanho janela

#3. Adicionar elementos (widgets)
lbl_titulo = Label(janela, text = "Cadastro de Usuário", pady=15).pack()
lbl_nome = Label(janela, text = "Nome:").pack()
txt_nome = Entry(janela)
txt_nome.pack()

btn_salvar = Button(janela, text = "Salvar", command=mostrar_mensagem)
btn_salvar.pack()

lbl_resultado = Label(janela, pady=15)
lbl_resultado.pack()


#4. Mostrar janela
janela.mainloop()

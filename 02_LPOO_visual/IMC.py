import tkinter as tk
from tkinter import Label, Entry, Button, messagebox

def Calcular_IMC():
    nome = txt_nome.get()
    if(nome.strip()):
        messagebox.showinfo("Acesso ao sistema", f"Bem_vindo(a) {nome}")
    else:
        messagebox.showerror("Error", f"Informe seu nome!!")

    peso = txt_peso.get()
    if not peso.strip():
        messagebox.showerror("Error", f"Informe seu peso!!")
        return

    altura = txt_altura.get()
    if not altura.strip():
        messagebox.showerror("Error", f"Informe sua altura!!")
        return

    peso = float(peso)
    altura = float(altura)
    resultado_IMC = peso / (altura * altura)
    

    if(resultado_IMC < 18.5):
        classificacao =  (f"Abaixo do peso")
    elif(resultado_IMC <= 24.9):
        classificacao = (f"Peso normal")
    elif(resultado_IMC <= 29.9):
        classificacao = (f"Sobrepeso")
    else:
        classificacao = (f"Obesidade")
    
    lbl_resultado.config(text=f"Seu IMC é {resultado_IMC:.2f}\nClassificação: {classificacao}")

    txt_nome.delete(0, tk.END)
    txt_peso.delete(0, tk.END)
    txt_altura.delete(0, tk.END)

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

lbl_peso = Label(janela, text = "Peso:").pack()
txt_peso = Entry(janela)
txt_peso.pack()

lbl_altura = Label(janela, text = "Altura:").pack()
txt_altura = Entry(janela)
txt_altura.pack()

btn_salvar = Button(janela, text = "Calcular IMC", command=Calcular_IMC)
btn_salvar.pack()

lbl_resultado = Label(janela, pady=15)
lbl_resultado.pack()


#4. Mostrar janela
janela.mainloop()
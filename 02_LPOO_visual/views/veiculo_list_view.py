import tkinter as tk
from tkinter import Label, Entry, Button, messagebox, Listbox
from tkinter import ttk


#1. criar a janela
janela = tk.Tk()

#2. Configurar a janela
janela.title("Lista de Veículos")
janela.geometry("600x400")

#3. Adicionar elementos (widgets)
lbl_titulo = Label(janela, text = "Lista de Veículos", pady=15).pack()

# ===== TABELA =====
colunas = ("placa", "tipo", "categoria", "taxa")

tree = ttk.Treeview(janela, columns=colunas, show="headings")
tree.pack(fill="both", expand=True)

# Cabeçalhos
tree.heading("placa", text="Placa")
tree.heading("tipo", text="Tipo")
tree.heading("categoria", text="Categoria")
tree.heading("taxa", text="Taxa")

# Dados iniciais
tree.insert("", tk.END, values=("ABC1234", "Carro", "ECONOMICO", "R$100"))
tree.insert("", tk.END, values=("XYZ9999", "Motorhome", "EXECUTIVO", "R$300"))


#FUNCOES

def exibir_dados(valores):
    placa, tipo, categoria, taxa = valores

    mensagem = f"Placa: {placa}\nTipo: {tipo}\nCategoria: {categoria}\nTaxa: {taxa}"
    messagebox.showinfo("Detalhes do Veículo", mensagem)

def ver_detalhes():
    selecionado = tree.selection()
    
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um veículo!")
        return
    
    item = selecionado[0]
    valores = tree.item(item, "values")
    
    exibir_dados(valores)

def remover():
    selecionado = tree.selection()
    
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um veículo para remover!")
        return
    
    tree.delete(selecionado)

def novo():
    nova_janela = tk.Toplevel(janela)
    nova_janela.title("Novo Veículo")
    nova_janela.geometry("300x300")

    #PLACA
    lbl_placa = Label(nova_janela, text="Placa:").pack()
    txt_placa = Entry(nova_janela)
    txt_placa.pack(pady=5)

    #TIPO
    lbl_tipo = Label(nova_janela, text="Tipo do Veículo:").pack()
    txt_tipo = ttk.Combobox(nova_janela, values=["Carro", "Motorhome"])
    txt_tipo.pack(pady=5)

    #CATEGORIA
    lbl_categoria = Label(nova_janela, text="Categoria:").pack()
    txt_categoria = ttk.Combobox(nova_janela, values=["Econômico", "Executivo"])
    txt_categoria.pack(pady=5)

    #TAXA
    lbl_taxa = Label(nova_janela, text="Taxa:").pack()
    txt_taxa = Entry(nova_janela)   
    txt_taxa.pack(pady=5)

    def salvar_veiculo():
        placa = txt_placa.get()
        tipo = txt_tipo.get()
        categoria = txt_categoria.get()
        taxa = txt_taxa.get()

        if not placa or not tipo or not categoria or not taxa:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        
        try:
            taxa_float = float(taxa)
        except ValueError:
            messagebox.showerror("Erro", "A taxa deve ser um número válido!")
            return
        
        tree.insert("", tk.END, values=(placa, tipo, categoria, f"R${taxa_float:.2f}"))
        messagebox.showinfo("Sucesso", "Veículo cadastrado!")
        nova_janela.destroy()  

    btn_salvar = Button(nova_janela, text="Salvar", command=salvar_veiculo)
    btn_salvar.pack(pady=10)




# Conteúdo principal
conteudo = tk.Frame(janela)
conteudo.pack(expand=True, fill="both")

# Rodapé
rodape = tk.Frame(janela)
rodape.pack(side=tk.BOTTOM, fill="x", pady=12)

botao = tk.Button(rodape, text="NOVO", command=novo)
botao.pack(side=tk.LEFT, padx=5, pady=10)

botao = tk.Button(rodape, text="VER DETALHES", command=ver_detalhes)
botao.pack(side=tk.LEFT, pady=10)

botao = tk.Button(rodape, text="REMOVER", command=remover)
botao.pack(side=tk.LEFT, pady=10)

#Mostrar janela
janela.mainloop()
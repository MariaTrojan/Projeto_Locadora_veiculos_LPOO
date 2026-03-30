import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
from tkinter import ttk

#IMPORT MODEL
from model.veiculo import VeiculoFactory, Categoria
from model.ExcecoesPersonalizadas import PlacaInvalidaError
from model.veiculo import Categoria

#LISTA
lista_veiculos = []

#JANELA
janela = tk.Tk()
janela.title("Lista de Veículos")
janela.geometry("600x400")

Label(janela, text="Lista de Veículos", pady=15).pack()

#TABELA
colunas = ("placa", "tipo", "categoria", "taxa")

tree = ttk.Treeview(janela, columns=colunas, show="headings")
tree.pack(fill="both", expand=True)

tree.heading("placa", text="Placa")
tree.heading("tipo", text="Tipo")
tree.heading("categoria", text="Categoria")
tree.heading("taxa", text="Taxa")

#FUNÇÕES

def atualizar_tabela():
    for item in tree.get_children():
        tree.delete(item)

    for v in lista_veiculos:
        tree.insert("", tk.END, values=(
            v.placa,
            v.__class__.__name__,
            v.categoria.value,
            f"R${v.taxa_diaria:.2f}"
        ))

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

    item = selecionado[0]
    valores = tree.item(item, "values")
    placa = valores[0]

    # remove da lista de objetos
    for v in lista_veiculos:
        if v.placa == placa:
            lista_veiculos.remove(v)
            break

    atualizar_tabela()

def novo():
    nova_janela = tk.Toplevel(janela)
    nova_janela.title("Novo Veículo")
    nova_janela.geometry("300x300")

    # PLACA
    Label(nova_janela, text="Placa:").pack()
    txt_placa = Entry(nova_janela)
    txt_placa.pack(pady=5)

    # TIPO
    Label(nova_janela, text="Tipo do Veículo:").pack()
    txt_tipo = ttk.Combobox(nova_janela, values=["Carro", "Motorhome"], state="readonly")
    txt_tipo.pack(pady=5)

    # CATEGORIA
    Label(nova_janela, text="Categoria:").pack()
    txt_categoria = ttk.Combobox(nova_janela, values=["ECONOMICO", "EXECUTIVO"], state="readonly")
    txt_categoria.pack(pady=5)

    # TAXA
    Label(nova_janela, text="Taxa:").pack()
    txt_taxa = Entry(nova_janela)
    txt_taxa.pack(pady=5)

    def salvar_veiculo():
        placa = txt_placa.get().strip()
        tipo = txt_tipo.get().strip()
        categoria_str = txt_categoria.get().strip()
        taxa = txt_taxa.get().strip()

        if not placa or not tipo or not categoria_str or not taxa:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        try:
            taxa_float = float(taxa)
        except ValueError:
            messagebox.showerror("Erro", "A taxa deve ser um número válido!")
            return

        #(STRING → ENUM)
        try:
            categoria = Categoria[categoria_str]
        except KeyError:
            messagebox.showerror("Erro", "Categoria inválida!")
            return

        #criar veículo usando Factory
        try:
            veiculo = VeiculoFactory.criar_veiculo(
                tipo,             
                placa,
                categoria,
                taxa_float
            )
        except PlacaInvalidaError as e:
            messagebox.showerror("Erro", str(e))
            return
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            return

        lista_veiculos.append(veiculo)

        atualizar_tabela()

        messagebox.showinfo("Sucesso", "Veículo cadastrado!")

        nova_janela.destroy()

    Button(nova_janela, text="Salvar", command=salvar_veiculo).pack(pady=10)

#RODAPÉ
rodape = tk.Frame(janela)
rodape.pack(side=tk.BOTTOM, fill="x", pady=12)

Button(rodape, text="NOVO", command=novo).pack(side=tk.LEFT, padx=5)
Button(rodape, text="VER INFORMAÇÕES", command=ver_detalhes).pack(side=tk.LEFT, padx=5)
Button(rodape, text="REMOVER", command=remover).pack(side=tk.LEFT, padx=5)

lista_veiculos.append(
    VeiculoFactory.criar_veiculo("Carro", "ABC1234", Categoria.ECONOMICO, 100)
)

lista_veiculos.append(
    VeiculoFactory.criar_veiculo("Motorhome", "XYZ9999", Categoria.EXECUTIVO, 300)
)

atualizar_tabela()

janela.mainloop()
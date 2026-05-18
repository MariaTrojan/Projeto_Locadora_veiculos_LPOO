import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk
from control.locacao_controller import LocacaoController
from model.locacao import StatusLocacao

class TelaLocacoesAdmin(tk.Toplevel):

    def __init__(self, master=None):
        super().__init__(master)
        self.controller = LocacaoController()

        self.title("Admin - Locações")

        self.criar_componentes()
        self.carregar_locacoes()

    def criar_componentes(self):
    
        #TABELA
        self.lista = ttk.Treeview(
            self,
            columns=("id", "placa", "inicio", "fim", "status"),
            show="headings"
        )

        self.lista.heading("id", text="ID")
        self.lista.heading("placa", text="Placa")
        self.lista.heading("inicio", text="Início")
        self.lista.heading("fim", text="Fim")
        self.lista.heading("status", text="Status")

        self.lista.pack(fill="both", expand=True)

        #BOTÕES
        frame = tk.Frame(self)
        frame.pack(pady=10)

        tk.Button(frame, text="Adicionar", command=self.adicionar).pack(side="left", padx=5)
        tk.Button(frame, text="Editar", command=self.editar).pack(side="left", padx=5)
        tk.Button(frame, text="Remover", command=self.remover).pack(side="left", padx=5)
        tk.Button(frame, text="Visualizar", command=self.visualizar).pack(side="left", padx=5)


    def carregar_locacoes(self):
        self.lista.delete(*self.lista.get_children())

        locacoes = self.controller.listar_locacoes()

        for loc in locacoes:
            self.lista.insert("", "end", values=(
                loc.id,
                loc.veiculo.placa,
                loc.data_inicio,
                loc.data_fim,
                loc.status.value
            ))

    def get_selecionado(self):
        item = self.lista.selection()

        if not item:
            from tkinter import messagebox
            messagebox.showwarning("Aviso", "Selecione uma locação", parent=self)
            return None

        valores = self.lista.item(item, "values")
        id_loc = valores[0]

        return self.controller.buscar_por_id(id_loc)

    
    def remover(self):
        loc = self.get_selecionado()

        if not loc:
            return

        sucesso, msg = self.controller.remover_locacao(loc.id)

        from tkinter import messagebox

        if sucesso:
            messagebox.showinfo("Sucesso", msg, parent=self)
            self.carregar_locacoes()
        else:
            messagebox.showerror("Erro", msg, parent=self)
    
    def adicionar(self):
        from view.janela_cadastro_locacao import JanelaCadastroLocacao

        janela = JanelaCadastroLocacao(self)
        self.wait_window(janela)
        self.carregar_locacoes()

    def editar(self):
        loc = self.get_selecionado()
        if not loc:
            return

        from view.janela_cadastro_locacao import JanelaCadastroLocacao

        janela = JanelaCadastroLocacao(self, locacao=loc)
        self.wait_window(janela)
        self.carregar_locacoes()

    def visualizar(self):
        loc = self.get_selecionado()

        if loc:
            from tkinter import messagebox
            msg = self.controller.ver_detalhes(loc)
            messagebox.showinfo("Detalhes", msg, parent=self)
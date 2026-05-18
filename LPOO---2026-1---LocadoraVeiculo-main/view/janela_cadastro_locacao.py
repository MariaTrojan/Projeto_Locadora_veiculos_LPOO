import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from control.locacao_controller import LocacaoController
from model.locacao import StatusLocacao


class JanelaCadastroLocacao(tk.Toplevel):

    def __init__(self, master=None, locacao=None):
        super().__init__(master)

        self.title("Cadastro de Locação")
        self.geometry("400x350")

        self.controller = LocacaoController()
        self.locacao = locacao  # se vier, é edição

        self.criar_componentes()
        self.preencher_campos()

    def criar_componentes(self):

        # PLACA
        tk.Label(self, text="Placa do Veículo").pack()
        self.entry_placa = tk.Entry(self)
        self.entry_placa.pack()

        # DATA INICIO
        tk.Label(self, text="Data Início (YYYY-MM-DD)").pack()
        self.entry_inicio = tk.Entry(self)
        self.entry_inicio.pack()

        # DATA FIM
        tk.Label(self, text="Data Fim (YYYY-MM-DD)").pack()
        self.entry_fim = tk.Entry(self)
        self.entry_fim.pack()

        # STATUS
        tk.Label(self, text="Status").pack()
        self.combo_status = ttk.Combobox(
            self,
            values=[s.value for s in StatusLocacao],
            state="readonly"
)
        self.combo_status.pack()

        # BOTÃO SALVAR
        tk.Button(self, text="Salvar", command=self.salvar).pack(pady=15)

    def preencher_campos(self):
        if self.locacao:
            self.entry_placa.insert(0, self.locacao.veiculo.placa)
            self.entry_inicio.insert(0, str(self.locacao.data_inicio))
            
            if self.locacao.data_fim:
                self.entry_fim.insert(0, str(self.locacao.data_fim))

            self.combo_status.set(self.locacao.status.value)
        else:
            self.combo_status.set(StatusLocacao.RESERVADO.value)

    def salvar(self):
        placa = self.entry_placa.get()
        data_inicio_str = self.entry_inicio.get()
        data_fim_str = self.entry_fim.get()
        status_str = self.combo_status.get()

        try:
            data_inicio = datetime.strptime(data_inicio_str, "%Y-%m-%d").date()

            data_fim = None
            if data_fim_str:
                data_fim = datetime.strptime(data_fim_str, "%Y-%m-%d").date()

            # validação básica (admin ainda precisa disso)
            if data_fim and data_inicio > data_fim:
                messagebox.showerror("Erro", "Data início deve ser <= data fim", parent=self)
                return

            # =========================
            # NOVA LOCAÇÃO
            # =========================
            if not self.locacao:
                sucesso, msg = self.controller.criar_locacao_admin(
                    placa,
                    data_inicio,
                    data_fim,
                    status_str
                )

            # =========================
            # EDIÇÃO
            # =========================
            else:
                self.locacao.data_inicio = data_inicio
                self.locacao.data_fim = data_fim
                self.locacao.status = StatusLocacao(status_str)

                sucesso, msg = self.controller.atualizar_locacao_admin(self.locacao)

            if sucesso:
                messagebox.showinfo("Sucesso", msg, parent=self)
                self.destroy()
            else:
                messagebox.showerror("Erro", msg, parent=self)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro: {e}", parent=self)
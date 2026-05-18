import tkinter as tk
from tkinter import ttk, messagebox
from control.locacao_controller import LocacaoController
from datetime import datetime

class JanelaNovaReserva(tk.Toplevel):

    def __init__(self, master=None):
        super().__init__(master)

        self.title("Nova Reserva")
        self.geometry("400x300")

        self.controller = LocacaoController()

        self.criar_componentes()

    def criar_componentes(self):

        tk.Label(self, text="Data Início (YYYY-MM-DD)").pack()
        self.entry_inicio = tk.Entry(self)
        self.entry_inicio.pack()

        tk.Label(self, text="Data Fim (YYYY-MM-DD)").pack()
        self.entry_fim = tk.Entry(self)
        self.entry_fim.pack()

        tk.Label(self, text="Categoria").pack()
        self.combo_categoria = ttk.Combobox(self, values=["ECONOMICO", "EXECUTIVO", "LUXO"])
        self.combo_categoria.pack()

        tk.Button(self, text="Buscar Veículos", command=self.buscar_veiculos).pack(pady=5)

        self.lista = ttk.Combobox(self)
        self.lista.pack()

        tk.Button(self, text="Reservar", command=self.reservar).pack(pady=10)

    # BUSCAR VEÍCULOS
    def buscar_veiculos(self):
        

        try:
            data_inicio = datetime.strptime(self.entry_inicio.get(), "%Y-%m-%d").date()
            data_fim = datetime.strptime(self.entry_fim.get(), "%Y-%m-%d").date()
            categoria = self.combo_categoria.get()

            if data_inicio > data_fim:
                messagebox.showerror("Erro", "Data início deve ser menor que data fim", parent=self)
                return
            if not categoria:
                messagebox.showwarning("Aviso", "Selecione uma categoria", parent=self)
                return

            veiculos = self.controller.buscar_veiculos_disponiveis(
                data_inicio, data_fim, categoria
            )

            if not veiculos:
                messagebox.showwarning("Aviso", "Nenhum veículo disponível", parent=self)
                return

            self.veiculos_map = {v.placa: v for v in veiculos}
            self.lista['values'] = list(self.veiculos_map.keys())

        except Exception as e:
            messagebox.showerror("Erro", f"Dados inválidos: {e}", parent=self)

   
    # RESERVAR
    def reservar(self):
        try:
            placa = self.lista.get()

            if not placa:
                messagebox.showwarning("Aviso", "Selecione um veículo", parent=self)
                return

            data_inicio = datetime.strptime(self.entry_inicio.get(), "%Y-%m-%d").date()
            data_fim = datetime.strptime(self.entry_fim.get(), "%Y-%m-%d").date()

            sucesso, msg = self.controller.criar_locacao(
                placa, data_inicio, data_fim
            )

            if sucesso:
                messagebox.showinfo("Sucesso", msg, parent=self)
                self.destroy()
            else:
                messagebox.showerror("Erro", msg, parent=self)

        except Exception as e:
            messagebox.showerror("Erro", str(e), parent=self)
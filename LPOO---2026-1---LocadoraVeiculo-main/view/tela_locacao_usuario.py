import tkinter as tk
from tkinter import ttk, messagebox
from control.locacao_controller import LocacaoController
from model import locacao
from model.locacao import StatusLocacao
from datetime import date

class JanelaLocacaoUsuario(tk.Toplevel):

    def __init__(self, master=None):
        super().__init__(master)

        self.title("Locação de Veículos")
        self.geometry("800x400")

        self.controller = LocacaoController()

        self.criar_componentes()
        self.carregar_locacoes()


    def criar_componentes(self):

        self.lista = ttk.Treeview(
            self,
            columns=("id", "placa", "inicio", "fim", "status"),
            show="headings"
        )

        for col in ("id", "placa", "inicio", "fim", "status"):
            self.lista.heading(col, text=col)

        self.lista.pack(fill="both", expand=True)

        frame = tk.Frame(self)
        frame.pack(pady=10)

        tk.Button(frame, text="Nova Reserva", command=self.nova_reserva).pack(side="left", padx=5)
        tk.Button(frame, text="Locar", command=self.locar).pack(side="left", padx=5)
        tk.Button(frame, text="Devolver", command=self.devolver).pack(side="left", padx=5)
        tk.Button(frame, text="Cancelar", command=self.cancelar).pack(side="left", padx=5)
        tk.Button(frame, text="Ver Detalhes", command=self.ver_detalhes).pack(side="left", padx=5)


    def carregar_locacoes(self):
        for row in self.lista.get_children():
            self.lista.delete(row)

        self.locacoes = self.controller.listar_locacoes()

        for loc in self.locacoes:
            self.lista.insert("", "end", values=(
                loc.id,
                loc.veiculo.placa,
                loc.data_inicio,
                loc.data_fim,
                loc.status.value
            ))

    def get_locacao_selecionada(self):
        selecionado = self.lista.selection()

        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma locação", parent=self)
            return None

        item = self.lista.item(selecionado[0])
        id_locacao = item['values'][0]

        for loc in self.locacoes:
            if loc.id == id_locacao:
                return loc

        return None


    def nova_reserva(self):
        from view.tela_nova import JanelaNovaReserva

        janela = JanelaNovaReserva(self)
        self.wait_window(janela)

        self.carregar_locacoes()

    def locar(self):
        loc = self.get_locacao_selecionada()
        if not loc:
            return

        if loc.status != StatusLocacao.RESERVADO:
            messagebox.showerror("Erro", "Só pode locar reservas", parent=self)
            return

        if loc.data_inicio != date.today():
            loc.data_inicio = date.today()

        sucesso, msg = self.controller.retirar_veiculo(loc, loc.id)

        if sucesso:
            messagebox.showinfo("Sucesso", msg, parent=self)
        else:
            messagebox.showerror("Erro", msg, parent=self)

        self.carregar_locacoes()

    def devolver(self):
        loc = self.get_locacao_selecionada()
        if not loc:
            return

        sucesso, msg = self.controller.devolver_veiculo(loc, loc.id)

        if sucesso:
            messagebox.showinfo("Devolução", msg, parent=self)
        else:
            messagebox.showerror("Erro", msg, parent=self)

        self.carregar_locacoes()

    def cancelar(self):
        loc = self.get_locacao_selecionada()
        if not loc:
            return

        if loc.status != StatusLocacao.RESERVADO:
            messagebox.showerror("Erro", "Só pode cancelar reservas", parent=self)
            return

        sucesso, msg = self.controller.cancelar_reserva(loc, loc.id)
        if sucesso:
            messagebox.showinfo("Sucesso", msg, parent=self)
        else:
            messagebox.showerror("Erro", msg, parent=self)

        self.carregar_locacoes()
        
    def ver_detalhes(self):
        loc = self.get_locacao_selecionada()
        if not loc:
            return

        msg = self.controller.ver_detalhes(loc)
        messagebox.showinfo("Detalhes", msg, parent=self)
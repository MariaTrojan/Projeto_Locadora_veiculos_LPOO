import tkinter as tk

from view.veiculo_list_view import JanelaListagemVeiculos
from view.tela_locacoes_admin import TelaLocacoesAdmin
from view.tela_locacao_usuario import JanelaLocacaoUsuario


class JanelaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Sistema Locadora")
        self.geometry("600x400")

        self.criar_menu()

    def criar_menu(self):
        menubar = tk.Menu(self)

        # =========================
        # MENU CADASTRO
        # =========================
        menu_cadastro = tk.Menu(menubar, tearoff=0)
        menu_cadastro.add_command(
            label="Veículos",
            command=self.abrir_veiculos
        )
        menu_cadastro.add_command(
            label="Locações (Admin)",
            command=self.abrir_locacoes_admin
        )

        menubar.add_cascade(label="Cadastro", menu=menu_cadastro)

        # MENU AÇÃO
        menu_acao = tk.Menu(menubar, tearoff=0)
        menu_acao.add_command(
            label="Locar Veículo",
            command=self.abrir_locacao_usuario
        )

        menubar.add_cascade(label="Ação", menu=menu_acao)

        self.config(menu=menubar)

    # TELAS
    def abrir_veiculos(self):
        janela = JanelaListagemVeiculos(self)
        self.wait_window(janela)

    def abrir_locacoes_admin(self):
        janela = TelaLocacoesAdmin(self)
        self.wait_window(janela)

    def abrir_locacao_usuario(self):
        janela = JanelaLocacaoUsuario(self)
        self.wait_window(janela)


# EXECUÇÃO
if __name__ == "__main__":
    app = JanelaPrincipal()
    app.mainloop()
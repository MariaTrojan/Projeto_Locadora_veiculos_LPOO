from dao.locacao_dao import LocacaoDAO
from dao.veiculo_dao import VeiculoDAO
from model import locacao
from model.locacao import Locacao, StatusLocacao
from datetime import date

class LocacaoController:
    
    def __init__(self):
        self.locacao_dao = LocacaoDAO()
        self.veiculo_dao = VeiculoDAO()
        
        
    def criar_locacao(self, placa: str, data_inicio, data_fim=None):
        if not placa or not data_inicio:
            return False, "Preencha os campos obrigatórios"
        
        try:
            veiculo = self.veiculo_dao.buscar_por_placa(placa.strip().upper())
            
            if not veiculo:
                return False, "Veículo não encontrado"
            
            locacao = Locacao(
                veiculo=veiculo,
                data_inicio=data_inicio,
                data_fim=data_fim
            )
            
            sucesso, msg = self.locacao_dao.salvar(locacao)
            return sucesso, msg
        
        except Exception as e:
            return False, f"Erro ao criar locação: {e}"
    
    
    def listar_locacoes(self):
        try:
            return self.locacao_dao.listar_todos()
        
        except Exception as e:
            print(f"Erro ao listar locações: {e}")
            return None
    
    
    def retirar_veiculo(self, locacao, id_locacao):
        try:
            if locacao.status != StatusLocacao.RESERVADO:
                return False, "Só é possível locar reservas"
        
            hoje = date.today()

            if locacao.data_inicio != hoje:
                locacao.data_inicio = hoje 
        
            locacao.retirar_veiculo()

            return self.locacao_dao.atualizar(locacao, id_locacao)
        except Exception as e:
            return False, f"Erro ao locar: {e}"
    
    
    def devolver_veiculo(self, locacao, id_locacao):
        try:
            if locacao.status != StatusLocacao.LOCADO:
                return False, "Locação não está ativa"

            hoje = date.today()

            if locacao.data_inicio >= hoje:
                return False, "Data de início inválida para devolução"

            locacao.data_fim = hoje
            locacao.devolver_veiculo()

            valor = locacao.calcular_valor_locacao()

            dias = (locacao.data_fim - locacao.data_inicio).days
            if dias <= 0:
                dias = 1

            self.locacao_dao.atualizar(locacao, id_locacao)

            msg = f"""
    Devolução realizada:
    Início: {locacao.data_inicio}
    Fim: {locacao.data_fim}
    Diárias: {dias}
    Valor total: R$ {valor:.2f}
    """
            return True, msg

        except Exception as e:
            return False, f"Erro ao devolver: {e}"
    
    
    def cancelar_reserva(self, locacao, id_locacao):
        try:
            if locacao.status != StatusLocacao.RESERVADO:
                return False, "Só é possível cancelar reservas"

            locacao.cancelar_reserva()

            return self.locacao_dao.atualizar(locacao, id_locacao)

        except Exception as e:
            return False, f"Erro ao cancelar: {e}"
    
    
    def remover_locacao(self, id_locacao):
        try:
            return self.locacao_dao.remover(id_locacao)
        
        except Exception as e:
            return False, f"Erro ao remover locação: {e}"
        
    def ver_detalhes(self, locacao):
        try:
            if locacao.status == StatusLocacao.DEVOLVIDO:
                dias = (locacao.data_fim - locacao.data_inicio).days
                if dias <= 0:
                    dias = 1

                valor = locacao.calcular_valor_locacao()

                return f"""
    Status: Devolvida
    Início: {locacao.data_inicio}
    Devolução: {locacao.data_fim}
    Diárias: {dias}
    Valor total: R$ {valor:.2f}
    """

            elif locacao.status in [StatusLocacao.RESERVADO, StatusLocacao.LOCADO]:
                valor = locacao.calcular_valor_locacao()

                return f"""
    Status: {locacao.status.value}
    Início: {locacao.data_inicio}
    Previsão: {locacao.data_fim}
    Valor estimado: R$ {valor:.2f}
    """

            elif locacao.status == StatusLocacao.CANCELADO:
                return f"""
    Status: Cancelada
    Início: {locacao.data_inicio}
    (Locação cancelada — sem cobrança)
    """

        except Exception as e:
            return f"Erro ao exibir detalhes: {e}"


    def criar_locacao_admin(self, placa, data_inicio, data_fim, status):
        try:
            veiculo = self.veiculo_dao.buscar_por_placa(placa)

            if not veiculo:
                return False, "Veículo não encontrado"

            if data_fim and data_inicio > data_fim:
                return False, "Data início deve ser <= data fim"

            loc = Locacao(
                veiculo=veiculo,
                data_inicio=data_inicio,
                data_fim=data_fim,
                status=StatusLocacao(status)
            )

            return self.locacao_dao.salvar(loc)

        except Exception as e:
            return False, str(e)
        
    def atualizar_locacao_admin(self, locacao):
        try:
            if locacao.data_fim and locacao.data_inicio > locacao.data_fim:
                return False, "Data início deve ser <= data fim"

            return self.locacao_dao.atualizar(locacao, locacao.id)

        except Exception as e:
            return False, str(e)
        
    def buscar_veiculos_disponiveis(self, data_inicio, data_fim, categoria):
        return self.locacao_dao.buscar_veiculos_disponiveis(
            data_inicio, data_fim, categoria
        )
    
    def buscar_por_id(self, id_locacao):
        return self.locacao_dao.buscar_por_id(id_locacao)
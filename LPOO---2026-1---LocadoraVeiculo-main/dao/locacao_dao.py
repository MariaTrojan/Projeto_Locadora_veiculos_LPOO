import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.locacao import Locacao, StatusLocacao
from dao.db_config import DatabaseConfig
from dao.generic_dao import GenericDAO
from dao.veiculo_dao import VeiculoDAO

class LocacaoDAO(GenericDAO):
    
    def __init__(self):
        self.conexao = DatabaseConfig.get_connection()
        self.veiculo_dao = VeiculoDAO()
        
    def salvar(self, locacao: Locacao):
        if not self.conexao:
            raise Exception("Sem conexão com o BD")
        
        try:
            cursor = self.conexao.cursor()
            query = """INSERT INTO tb_locacoes
            (loc_veiculo_placa, loc_data_inicio, loc_data_fim, loc_status)
            VALUES (%s, %s, %s, %s)"""
            
            cursor.execute(query, (
                locacao.veiculo.placa,
                locacao.data_inicio,
                locacao.data_fim,
                locacao.status.value
                
            ))
            
            self.conexao.commit()
            return True, "Locação cadastrada com sucesso"
                                
        except Exception as e:
            print(f"Erro ao inserir locação: {e}")
            self.conexao.rollback()
            return False, f"Erro ao inserir locação: {e}"
        
        finally:
            if cursor:
                cursor.close()


    def listar_todos(self):
        if not self.conexao:
            return []
        
        try:
            cursor = self.conexao.cursor()
            query = """SELECT loc_id, loc_veiculo_placa, loc_data_inicio, loc_data_fim, loc_status
                       FROM tb_locacoes"""
            cursor.execute(query)
            linhas = cursor.fetchall()
            
            locacoes = []
            
            for linha in linhas:
                veiculo = self.veiculo_dao.buscar_por_placa(linha[1])
                
                loc = Locacao(
                    veiculo=veiculo,
                    data_inicio=linha[2],
                    data_fim=linha[3],
                    id_locacao=linha[0],
                    status=StatusLocacao(linha[4])
                )
                
                loc.status = StatusLocacao(linha[4])
                
                locacoes.append(loc)
            
            return locacoes
                                
        except Exception as e:
            print(f"Erro ao buscar locações: {e}")
            return []
        
        finally:
            if cursor:
                cursor.close()


    def atualizar(self, locacao: Locacao, id_locacao: int):
        if not self.conexao:
            return False, "Sem conexão com o BD"
        
        try:
            cursor = self.conexao.cursor()
            query = """UPDATE tb_locacoes 
                       SET loc_data_inicio = %s,
                           loc_data_fim = %s,
                           loc_status = %s
                       WHERE loc_id = %s"""
            
            cursor.execute(query, (
                locacao.data_inicio,
                locacao.data_fim,
                locacao.status.value,
                id_locacao
            ))
            
            self.conexao.commit()
            return True, "Locação atualizada com sucesso"
            
        except Exception as e:
            print(f"Erro ao atualizar locação: {e}")
            self.conexao.rollback()
            return False, f"Erro ao atualizar locação: {e}"
        
        finally:
            if cursor:
                cursor.close()


    def remover(self, id_locacao: int):
        if not self.conexao:
            return False, "Sem conexão com o BD"
        
        try:
            cursor = self.conexao.cursor()
            query = "DELETE FROM tb_locacoes WHERE loc_id = %s"
            cursor.execute(query, (id_locacao,))
            
            self.conexao.commit()
            return True, "Locação removida com sucesso"
            
        except Exception as e:
            print(f"Erro ao remover locação: {e}")
            self.conexao.rollback()
            return False, f"Erro ao remover locação: {e}"
        
        finally:
            if cursor:
                cursor.close()


    def buscar_por_id(self, id_locacao: int):
        if not self.conexao:
            return None
        
        try:
            cursor = self.conexao.cursor()
            query = """SELECT loc_id, loc_veiculo_placa, loc_data_inicio, loc_data_fim, loc_status
                       FROM tb_locacoes
                       WHERE loc_id = %s"""
            
            cursor.execute(query, (id_locacao,))
            linha = cursor.fetchone()
            
            if linha:
                veiculo = self.veiculo_dao.buscar_por_placa(linha[1])
                
                loc = Locacao(
                    veiculo=veiculo,
                    data_inicio=linha[2],
                    data_fim=linha[3]
                )
                
                loc.status = StatusLocacao(linha[4])
                
                return loc
            
            return None
            
        except Exception as e:
            print(f"Erro ao buscar locação: {e}")
        
        finally:
            if cursor:
                cursor.close()

    def buscar_veiculos_disponiveis(self, data_inicio, data_fim, categoria):
        if not self.conexao:
            return []

        try:
            cursor = self.conexao.cursor()

            query = """
            SELECT v.vei_placa, v.vei_categoria, v.vei_taxa_diaria, v.vei_tipo
            FROM tb_veiculos v
            WHERE v.vei_categoria = %s
            AND v.vei_placa NOT IN (
                SELECT l.loc_veiculo_placa
                FROM tb_locacoes l
                WHERE l.loc_status IN ('reservado', 'locado')
                AND NOT (
                    l.loc_data_fim < %s OR l.loc_data_inicio > %s
)
            )
            """

            cursor.execute(query, (categoria, data_inicio, data_fim))
            linhas = cursor.fetchall()

            veiculos = []

            from model.veiculo import VeiculoFactory

            for linha in linhas:
                obj = VeiculoFactory.criar_veiculo(
                    linha[3], linha[0], linha[1], float(linha[2])
                )
                veiculos.append(obj)

            return veiculos

        except Exception as e:
            print(f"Erro ao buscar veículos disponíveis: {e}")
            return []

        finally:
            if cursor:
                cursor.close()
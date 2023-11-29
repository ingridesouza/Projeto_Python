import sqlite3
import os

class RoomDB:
    CREATE_TABLE_NOTA_FISCAL = 'CREATE TABLE IF NOT EXISTS nota_fiscal(id INTEGER PRIMARY KEY AUTOINCREMENT, check_in_date text, total float, valor_unitario float)'
    INSERT_REGISTRO_QUERY = 'INSERT INTO nota_fiscal(check_in_date) VALUES (?)'
    SELECT_NAME_FROM_TABLE = 'SELECT nome_cliente FROM clientes WHERE numero_mesa = ?'

    def __init__(self):
        self.connection = sqlite3.connect("bancoRestaurante.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.CREATE_TABLE_NOTA_FISCAL)
        self.connection.commit()
        print("Tabelas criadas com sucesso!")

    def inserir_data(self, check_in_date):
        self.cursor.execute(self.INSERT_REGISTRO_QUERY, (check_in_date,))
        print("Data adicionada com sucesso!")
        self.connection.commit()






    def inserir_total(self, total):
        # Inserir dados na tabela pratos
        self.cursor.execute('INSERT INTO pratos(total) VALUES (?, ?)', (total))
        self.connection.commit()

    def inserir_valor(self, nome_cliente, total):
        # Inserir dados na tabela pratos
        self.cursor.execute('INSERT INTO cliente(nome_cliente, total) VALUES (?, ?)', (nome_cliente, total))
        self.connection.commit()

    def fechar_registro(self, numero_mesa, status_da_conta):
        # Verificar se a mesa está aberta antes de fechar
        self.cursor.execute(self.INSERT_REGISTRO_QUERY(numero_mesa, status_da_conta))
        registro_aberto = self.cursor.fetchone()

        if registro_aberto:
            # Calcular o total (pode ser mais complexo dependendo dos detalhes do seu sistema)
            total = 0.0  # Substitua isso pela lógica real de cálculo do total

            # Atualizar a nota fiscal com o status da conta fechada e o total
            self.cursor.execute('UPDATE nota_fiscal SET status_da_conta = false, total = ? WHERE status_da_conta = ?', (total, status_da_conta))
            self.connection.commit()
            print(f"Registro da mesa {status_da_conta} fechado com sucesso.")
        else:
            print(f"Registro da mesa {status_da_conta} não encontrado ou já está fechado.")


    def __del__(self):
        # Fechar a conexão com o banco de dados
        self.connection.close()


# Exemplo de uso no tkinter, podem chamar essas funções passando os parâmetros que o usuário fornece
#vcs podem olhar no código do colega de giovanna henrique nesse link: https://github.com/PythonProjectWyden/Front-end/blob/main/Tela_Principal/tela_inicio.py


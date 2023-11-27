import sqlite3
import os

class RoomDB:
    def __init__(self, db_name='Banco.db'):
        # Obtém o caminho do diretório onde o script Python está sendo executado
        caminho_atual = os.path.dirname(os.path.abspath(__file__))
        
        # Junta o caminho do diretório com o nome do arquivo do banco de dados/cria o banco no mesmo diretório
        #se vcs rodarem o código vão perceber que um banco vai ser criado na máquina de vocês 
        self.caminho_banco = os.path.join(caminho_atual, db_name)
        
        # Conecta ao banco de dados
        self.conn = sqlite3.connect(self.caminho_banco)
        self.cursor = self.conn.cursor()

        # Chama a função para criar as tabelas 
        self.criar_tabelas()

    def criar_tabelas(self):
        # Tabela pratos
        self.cursor.execute('CREATE TABLE IF NOT EXISTS pratos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome_prato TEXT, valor FLOAT)')

        # Tabela clientes
        self.cursor.execute('CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome_cliente TEXT, registro_de_pratos INTEGER, FOREIGN KEY (registro_de_pratos) REFERENCES pratos(id))')

        # Tabela nota fiscal, o status da conta seria como true para aberto e falso para fechado, na hora que o cliente sair
        #self.cursor.execute('CREATE TABLE IF NOT EXISTS nota_fiscal(id INTEGER PRIMARY KEY, status_da_conta as boolean, check_in_date DATE, numero_mesa INTEGER, total FLOAT, FOREIGN KEY (numero_mesa) REFERENCES pratos(id))')

        
        self.cursor.execute('CREATE TABLE IF NOT EXISTS nota_fiscal(id INTEGER PRIMARY KEY, status_da_conta INTEGER, check_in_date DATE, numero_mesa INTEGER, total FLOAT, cliente_id INTEGER, FOREIGN KEY (numero_mesa) REFERENCES pratos(id), FOREIGN KEY (cliente_id) REFERENCES clientes(registro_de_pratos))')

        # Commit para salvar as alterações
        self.conn.commit()
        print("Tabelas criadas com sucesso!")

##------------- IMPORTANTE
#São essas funções que vão fazer o INSERIR, READ, UPDATE, DELETE do banco. Os parâmetros serão preenchidos
#com os dados que o usuário colocar na interface do tkinter que ingrid fez (index)
#falta criar: fechar registro (está no TK inter como fechar registro) é o mesmo que nota fiscar
#falta criar: criar registro (abrir nota fiscal)


    def inserir_total(self, total):
        # Inserir dados na tabela pratos
        self.cursor.execute('INSERT INTO pratos(total) VALUES (?, ?)', (total))
        self.conn.commit()

    def inserir_cliente(self, nome_cliente, numero_mesa):
        # Inserir dados na tabela clientes
        self.cursor.execute('INSERT INTO clientes(nome_cliente, numero_mesa) VALUES (?, ?)', (nome_cliente, numero_mesa))
        self.conn.commit()

    def inserir_valor(self, nome_cliente, registro_de_pratos):
        # Inserir dados na tabela pratos
        self.cursor.execute('INSERT INTO cliente(nome_cliente, registro_de_pratos) VALUES (?, ?)', (nome_cliente, registro_de_pratos))
        self.conn.commit()

    def fechar_conexao(self):
        # Fechar a conexão com o banco de dados
        self.conn.close()


# Exemplo de uso no tkinter, podem chamar essas funções passando os parâmetros que o usuário fornece
#vcs podem olhar no código do colega de giovanna victor nesse link: https://github.com/PythonProjectWyden/Front-end/blob/main/Tela_Principal/tela_inicio.py

room_db = RoomDB()
room_db.criar_tabelas()
room_db.inserir_prato('Prato1', 10.99)
room_db.inserir_cliente('Cliente1', 1)
room_db.fechar_conexao()

import sqlite3
import mysql.connector


class DataBase():
    def __init__(self, name = "system.db")-> None:
        self.name = name

    #def conecta(self):
    #    self.connection = sqlite3.connect(self.name)

    def conecta(self):
        self.connection = mysql.connector.connect(
            host = 'sys_cad.mysql.dbaas.com.br',
            user = 'sys_cad',
            passwd = 'f984745289F@',
            db = 'sys_cad'
        )
        cursor = self.connection.cursor()

    

        sql = 'SELECT * FROM matriz'

        cursor.execute(sql)
        resultados = cursor.fetchall()
        
        num_colunas = len(cursor.description)
        nome_colunas = [i[0] for i in cursor.description]

        dados = (resultados, nome_colunas)

        return dados


    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    #-------CRIA TABELA DE USUARIO------------------#
    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id	INTEGER,
                    cpf	TEXT NOT NULL,
                    nome	TEXT NOT NULL,
                    password	TEXT NOT NULL,
                    access	TEXT NOT NULL DEFAULT Usuario,
                    cod_sys	TEXT,
                    perfil	TEXT,
                    PRIMARY KEY(id)
                );

             """)
        except AttributeError:
            print("faça a conexão")

    #-------CRIA TABELA DE PERFIL------------------#
    def create_table_perfil(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS perfil (
                    id	INTEGER,
                    nome_perfil TEXT NOT NULL,
                    descricao	TEXT NOT NULL,                    
                    PRIMARY KEY(id)
                );

             """)
        except AttributeError:
            print("faça a conexão")

    #-------CRIA TABELA DE SISTEMA------------------#
    def create_table_sistema(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sistema (
                    id	INTEGER,
                    nome_sistema TEXT NOT NULL,
                    descricao	TEXT NOT NULL,                    
                    PRIMARY KEY(id)
                );

             """)
        except AttributeError:
            print("faça a conexão")


    #-------CRIA TABELA DE SISTEMA------------------#
    def create_table_matriz(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS matriz (
                    id	INTEGER,
                    cod_sys_1 TEXT NOT NULL,
                    nome_perfil_1	TEXT NOT NULL,   
                    cod_sys_2 TEXT NOT NULL,
                    nome_perfil_2	TEXT NOT NULL,                  
                    PRIMARY KEY(id)
                );

             """)
        except AttributeError:
            print("faça a conexão")
   


    def insert_user(self, cpf, nome, password, access, cod_sys, perfil):

        try:
            cursor = self.connection.cursor()
            sql = 'INSERT INTO users(`cpf`, `nome`, `password`, `access`, `cod_sys`, `perfil`) VALUES (%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql,(cpf, nome, password, access, cod_sys, perfil))
            self.connection.commit()
        except AttributeError:
            print("Faça a conexão")


    def insert_perfil(self, nome_perfil, descricao, codigo_perfil):

        try:
            cursor = self.connection.cursor()
            sql = 'INSERT INTO perfil(`nome_perfil`, `descricao`, `codigo_perfil`) VALUES (%s,%s,%s)'
            cursor.execute(sql,(nome_perfil, descricao, codigo_perfil))
            self.connection.commit()
        except AttributeError:
            print("Faça a conexão")

    def insert_sistema(self, nome_sistema, descricao, codigo_sistema):

        try:
            cursor = self.connection.cursor()
            sql = 'INSERT INTO sistema(`nome_sistema`, `descricao`, `codigo_sistema`) VALUES (%s,%s,%s)'
            cursor.execute(sql,(nome_sistema, descricao, codigo_sistema))
            self.connection.commit()
        except AttributeError:
            print("Faça a conexão")

    def check_user(self, cpf, password):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT * FROM users;
            """)

            for linha in cursor.fetchall():
                if linha[1].upper() == cpf.upper() and linha[3] == password and linha[4] == "Administrador":
                    return "Administrador"
                    
                elif linha[1].upper() == cpf.upper() and linha[3] == password and linha[4] == "Usuário":
                    return "user"
                else:
                    continue
            return "sem acesso"
        except:
            pass

if __name__== "__main__":

    db = DataBase()
    db.conecta()
    #db.create_table_users() 
    #db.create_table_perfil()  
    #db.create_table_sistema()   
    #db.create_table_matriz()  
    db.close_connection()



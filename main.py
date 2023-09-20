# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import*
from PySide6.QtGui import*
from PySide6.QtWidgets import*
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
from modelo import CustomTableModel
from database import DataBase

import sys

class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")

        self.btn_login.clicked.connect(self.checkLogin)


    def open_system(self):
        if self.txt_password.text() == '123':
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            print("senha invalida")


    def checkLogin(self):
        self.users = DataBase()
        self.users.conecta()
        autenticado = self.users.check_user(self.txt_usuario.text().upper(), self.txt_password.text())

        if autenticado.lower() == "administrador" or autenticado.lower() == "user":

            self.w = MainWindow(autenticado.lower())
            self.w.show()
            self.close()
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f'Login ou senha incorreto \n \n Tentativa: {self.tentativas +1} de 3')
                msg.exec_()
                self.tentativas += 1
            if self.tentativas == 3:
                #bloquear o usuário
                self.users.close_connection()
                sys.exit()



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")

        if user.lower() == "user":
            self.btn_pg_cadastrar_sistema.setVisible(False)
            self.btn_pg_cadastrar_perfil.setVisible(False)
            self.btn_pg_cadastro_usuario.setVisible(False)
            self.btn_pg_cadastrar_matriz.setVisible(False)
            self.btn_pg_consulta.setVisible(False)

        #========PAGINAS DO SISTEMA==========#
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_pg_consulta_2.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_consultas))
        self.btn_tables.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_table))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        self.btn_devteam9.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_devteam9))
        self.btn_pg_cadastrar_sistema.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_sistema))
        self.btn_pg_cadastrar_perfil.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_perfil))
        self.btn_pg_cadastro_usuario.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_usuario))
        self.btn_pg_cadastrar_matriz.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_matriz))
        self.btn_pg_consulta.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_consultas))

        self.btn_cadastrar_usuario.clicked.connect(self.subscribe_user)
        self.btn_cadastrar_perfil.clicked.connect(self.subscribe_perfil)
        self.btn_cadastrar_sistema.clicked.connect(self.subscribe_sistema)





    def subscribe_user(self):
        
        if self.txt_senha_usuario.text() != self.txt_senha_usuario_2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senhas divergentes")
            msg.setText("As senhas não conferem!")
            msg.exec_()
            return None
        
        cpf = self.txt_cpf_usuario.text()
        nome = self.txt_nome_usuario.text()
        password = self.txt_senha_usuario.text()
        sistema = self.cb_sistema_usuario.currentText()
        perfil = self.cb_perfil_usuario.currentText()
        access = self.cb_access_usuario.currentText()

        db = DataBase()
        db.conecta()
        db.insert_user(cpf, nome, password, sistema, perfil, access)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Cadastro de usuário")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()

        self.txt_cpf_usuario.setText("")
        self.txt_nome_usuario.setText("")
        self.txt_senha_usuario.setText("")
        self.txt_senha_usuario_2.setText("")


    def subscribe_perfil(self):       
           
        perfil_nome = self.txt_nome_perfil.text()
        perfil_descricao = self.txt_descricao_perfil.text()
        perfil_codigo = self.txt_codigo_perfil.text()
       

        db = DataBase()
        db.conecta()
        db.insert_perfil(perfil_nome, perfil_descricao, perfil_codigo)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Cadastro de perfil")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()


    def subscribe_sistema(self):       
           
        sistema_nome = self.txt_nome_sistema.text()
        sistema_descricao = self.txt_sistema_descricao.text()
        sistema_codigo = self.txt_codigo_sistema.text()
       

        db = DataBase()
        db.conecta()
        db.insert_sistema(sistema_nome, sistema_descricao, sistema_codigo)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Cadastro de sistema")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()

        self.txt_nome_sistema.setText("")
        self.txt_sistema_descricao.setText("")
        self.txt_codigo_sistema.setText("")
        
        





if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()

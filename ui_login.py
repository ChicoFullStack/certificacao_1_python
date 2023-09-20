# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import*
from PySide6.QtGui import*
from PySide6.QtWidgets import*

class Ui_Login(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(204, 298)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 104, 201, 191))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_usuario = QLineEdit(self.frame)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setGeometry(QRect(20, 20, 161, 20))
        font = QFont()
        font.setPointSize(10)
        self.txt_usuario.setFont(font)
        self.txt_usuario.setAlignment(Qt.AlignCenter)
        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setGeometry(QRect(20, 66, 161, 20))
        self.txt_password.setFont(font)
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(30, 116, 141, 23))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.btn_login.setFont(font1)
        self.btn_login.setStyleSheet(u"QPushButton{		\n"
"	background-color: rgb(19, 193, 144);	\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	}\n"
"QPushButton:hover{		\n"
"	background-color: rgb(255, 255, 255);		\n"
"	border: 2px solid rgb(19, 193, 144);	\n"
"	color: rgb(20,0,0);		\n"
"   	}\n"
"")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 20, 81, 71))
        self.label_2.setPixmap(QPixmap(u"imgs/logoe.png"))
        self.label_2.setScaledContents(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Sistema", None))
#if QT_CONFIG(tooltip)
        self.txt_usuario.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("Form", u"Usu\u00e1rio", None))
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Form", u"Senha", None))
        self.btn_login.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label_2.setText("")
    # retranslateUi



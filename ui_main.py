# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 597)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 10);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_17 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 12px;\n"
"	font-size: 16px;	\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: #fff;\n"
"	color: black\n"
"}")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_pg_consulta_2 = QPushButton(self.frame)
        self.btn_pg_consulta_2.setObjectName(u"btn_pg_consulta_2")
        self.btn_pg_consulta_2.setMinimumSize(QSize(0, 30))
        self.btn_pg_consulta_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_consulta_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 12px;\n"
"	font-size: 16px;	\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: #fff;\n"
"	color: black\n"
"}")

        self.horizontalLayout.addWidget(self.btn_pg_consulta_2)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setMinimumSize(QSize(0, 30))
        self.btn_tables.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tables.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 12px;\n"
"	font-size: 16px;	\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: #fff;\n"
"	color: black\n"
"}")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 12px;\n"
"	font-size: 16px;	\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: #fff;\n"
"	color: black\n"
"}")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_devteam9 = QPushButton(self.frame)
        self.btn_devteam9.setObjectName(u"btn_devteam9")
        self.btn_devteam9.setMinimumSize(QSize(0, 30))
        self.btn_devteam9.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_devteam9.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 12px;\n"
"	font-size: 16px;	\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: #fff;\n"
"	color: black\n"
"}")

        self.horizontalLayout.addWidget(self.btn_devteam9)


        self.verticalLayout_17.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        sizePolicy.setHeightForWidth(self.Pages.sizePolicy().hasHeightForWidth())
        self.Pages.setSizePolicy(sizePolicy)
        self.Pages.setContextMenuPolicy(Qt.NoContextMenu)
        self.Pages.setStyleSheet(u"background-color: rgb(36, 31, 175);\n"
"background-color: rgb(74, 74, 74);")
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.label_2 = QLabel(self.pg_table)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(9, 9, 741, 25))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.Pages.addWidget(self.pg_table)
        self.pg_cadastro_sistema = QWidget()
        self.pg_cadastro_sistema.setObjectName(u"pg_cadastro_sistema")
        self.verticalLayout = QVBoxLayout(self.pg_cadastro_sistema)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_31 = QLabel(self.pg_cadastro_sistema)
        self.label_31.setObjectName(u"label_31")
        font1 = QFont()
        font1.setPointSize(17)
        self.label_31.setFont(font1)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_31)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(30, -1, 30, -1)
        self.label_30 = QLabel(self.pg_cadastro_sistema)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_19.addWidget(self.label_30)

        self.txt_nome_sistema = QLineEdit(self.pg_cadastro_sistema)
        self.txt_nome_sistema.setObjectName(u"txt_nome_sistema")
        self.txt_nome_sistema.setStyleSheet(u"color: rgba(211, 239, 251, 1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 115, 155, 0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_19.addWidget(self.txt_nome_sistema)


        self.verticalLayout.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(30, -1, 30, -1)
        self.label_29 = QLabel(self.pg_cadastro_sistema)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_18.addWidget(self.label_29)

        self.txt_sistema_descricao = QLineEdit(self.pg_cadastro_sistema)
        self.txt_sistema_descricao.setObjectName(u"txt_sistema_descricao")
        self.txt_sistema_descricao.setStyleSheet(u"color: rgba(211, 239, 251, 1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 115, 155, 0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_18.addWidget(self.txt_sistema_descricao)


        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(30, -1, 30, -1)
        self.label_34 = QLabel(self.pg_cadastro_sistema)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_22.addWidget(self.label_34)

        self.txt_codigo_sistema = QLineEdit(self.pg_cadastro_sistema)
        self.txt_codigo_sistema.setObjectName(u"txt_codigo_sistema")
        self.txt_codigo_sistema.setStyleSheet(u"color: rgba(211, 239, 251, 1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 115, 155, 0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_22.addWidget(self.txt_codigo_sistema)


        self.verticalLayout.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_32 = QLabel(self.pg_cadastro_sistema)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_20.addWidget(self.label_32)

        self.btn_cadastrar_sistema = QPushButton(self.pg_cadastro_sistema)
        self.btn_cadastrar_sistema.setObjectName(u"btn_cadastrar_sistema")
        self.btn_cadastrar_sistema.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar_sistema.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius: 8px;\n"
"	font-size: 16px;	\n"
"	background-color: #fff;\n"
"	color: black\n"
"\n"
"}\n"
"QPushButton:hover{	\n"
"	\n"
"	color: rgb(255, 255, 255);	\n"
"	background-color: rgb(0, 80, 121);\n"
"}")

        self.horizontalLayout_20.addWidget(self.btn_cadastrar_sistema)

        self.label_33 = QLabel(self.pg_cadastro_sistema)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_20.addWidget(self.label_33)


        self.verticalLayout.addLayout(self.horizontalLayout_20)

        self.Pages.addWidget(self.pg_cadastro_sistema)
        self.pg_cadastro_usuario = QWidget()
        self.pg_cadastro_usuario.setObjectName(u"pg_cadastro_usuario")
        self.verticalLayout_2 = QVBoxLayout(self.pg_cadastro_usuario)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_6 = QLabel(self.pg_cadastro_usuario)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_6)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(30, -1, 30, -1)
        self.label_14 = QLabel(self.pg_cadastro_usuario)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_12.addWidget(self.label_14)

        self.txt_cpf_usuario = QLineEdit(self.pg_cadastro_usuario)
        self.txt_cpf_usuario.setObjectName(u"txt_cpf_usuario")
        self.txt_cpf_usuario.setStyleSheet(u"color: rgba(211, 239, 251, 1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 115, 155, 0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_12.addWidget(self.txt_cpf_usuario)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(30, -1, 30, -1)
        self.label_7 = QLabel(self.pg_cadastro_usuario)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.txt_nome_usuario = QLineEdit(self.pg_cadastro_usuario)
        self.txt_nome_usuario.setObjectName(u"txt_nome_usuario")
        self.txt_nome_usuario.setStyleSheet(u"color: rgba(211, 239, 251, 1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 115, 155, 0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_9.addWidget(self.txt_nome_usuario)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(30, -1, 30, -1)
        self.label_9 = QLabel(self.pg_cadastro_usuario)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.txt_senha_usuario = QLineEdit(self.pg_cadastro_usuario)
        self.txt_senha_usuario.setObjectName(u"txt_senha_usuario")
        self.txt_senha_usuario.setStyleSheet(u"color: rgba(211, 239, 251, 1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 115, 155, 0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size:21px;")
        self.txt_senha_usuario.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.txt_senha_usuario)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(30, -1, 30, -1)
        self.label_10 = QLabel(self.pg_cadastro_usuario)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)

        self.txt_senha_usuario_2 = QLineEdit(self.pg_cadastro_usuario)
        self.txt_senha_usuario_2.setObjectName(u"txt_senha_usuario_2")
        self.txt_senha_usuario_2.setStyleSheet(u"color: rgba(211, 239, 251, 1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 115, 155, 0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size:21px;")
        self.txt_senha_usuario_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_8.addWidget(self.txt_senha_usuario_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(30, 10, 30, -1)
        self.label_17 = QLabel(self.pg_cadastro_usuario)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_16.addWidget(self.label_17)

        self.cb_sistema_usuario = QComboBox(self.pg_cadastro_usuario)
        self.cb_sistema_usuario.addItem("")
        self.cb_sistema_usuario.addItem("")
        self.cb_sistema_usuario.setObjectName(u"cb_sistema_usuario")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.cb_sistema_usuario.setFont(font2)
        self.cb_sistema_usuario.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_16.addWidget(self.cb_sistema_usuario)


        self.verticalLayout_2.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(30, 10, 30, -1)
        self.label_11 = QLabel(self.pg_cadastro_usuario)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)

        self.cb_perfil_usuario = QComboBox(self.pg_cadastro_usuario)
        self.cb_perfil_usuario.addItem("")
        self.cb_perfil_usuario.addItem("")
        self.cb_perfil_usuario.setObjectName(u"cb_perfil_usuario")
        self.cb_perfil_usuario.setFont(font2)
        self.cb_perfil_usuario.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.cb_perfil_usuario)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(30, 10, 30, -1)
        self.label_18 = QLabel(self.pg_cadastro_usuario)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_17.addWidget(self.label_18)

        self.cb_access_usuario = QComboBox(self.pg_cadastro_usuario)
        self.cb_access_usuario.addItem("")
        self.cb_access_usuario.addItem("")
        self.cb_access_usuario.setObjectName(u"cb_access_usuario")
        self.cb_access_usuario.setFont(font2)
        self.cb_access_usuario.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_17.addWidget(self.cb_access_usuario)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.pg_cadastro_usuario)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_11.addWidget(self.label_12)

        self.btn_cadastrar_usuario = QPushButton(self.pg_cadastro_usuario)
        self.btn_cadastrar_usuario.setObjectName(u"btn_cadastrar_usuario")
        self.btn_cadastrar_usuario.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar_usuario.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius: 8px;\n"
"	font-size: 16px;	\n"
"	background-color: #fff;\n"
"	color: black\n"
"\n"
"}\n"
"QPushButton:hover{	\n"
"	\n"
"	color: rgb(255, 255, 255);	\n"
"	background-color: rgb(0, 80, 121);\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_cadastrar_usuario)

        self.label_13 = QLabel(self.pg_cadastro_usuario)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_11.addWidget(self.label_13)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.Pages.addWidget(self.pg_cadastro_usuario)
        self.pg_cadastro_perfil = QWidget()
        self.pg_cadastro_perfil.setObjectName(u"pg_cadastro_perfil")
        self.verticalLayout_4 = QVBoxLayout(self.pg_cadastro_perfil)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_24 = QLabel(self.pg_cadastro_perfil)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_24)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(30, -1, 30, -1)
        self.label_25 = QLabel(self.pg_cadastro_perfil)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_14.addWidget(self.label_25)

        self.txt_nome_perfil = QLineEdit(self.pg_cadastro_perfil)
        self.txt_nome_perfil.setObjectName(u"txt_nome_perfil")
        self.txt_nome_perfil.setStyleSheet(u"color: rgba(211, 239, 251, 1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 115, 155, 0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_14.addWidget(self.txt_nome_perfil)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(30, -1, 30, -1)
        self.label_26 = QLabel(self.pg_cadastro_perfil)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_15.addWidget(self.label_26)

        self.txt_descricao_perfil = QLineEdit(self.pg_cadastro_perfil)
        self.txt_descricao_perfil.setObjectName(u"txt_descricao_perfil")
        self.txt_descricao_perfil.setStyleSheet(u"color: rgba(211, 239, 251, 1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 115, 155, 0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_15.addWidget(self.txt_descricao_perfil)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(30, -1, 30, -1)
        self.label_27 = QLabel(self.pg_cadastro_perfil)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_21.addWidget(self.label_27)

        self.txt_codigo_perfil = QLineEdit(self.pg_cadastro_perfil)
        self.txt_codigo_perfil.setObjectName(u"txt_codigo_perfil")
        self.txt_codigo_perfil.setStyleSheet(u"color: rgba(211, 239, 251, 1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 115, 155, 0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_21.addWidget(self.txt_codigo_perfil)


        self.verticalLayout_4.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_22 = QLabel(self.pg_cadastro_perfil)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_13.addWidget(self.label_22)

        self.btn_cadastrar_perfil = QPushButton(self.pg_cadastro_perfil)
        self.btn_cadastrar_perfil.setObjectName(u"btn_cadastrar_perfil")
        self.btn_cadastrar_perfil.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar_perfil.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius: 8px;\n"
"	font-size: 16px;	\n"
"	background-color: #fff;\n"
"	color: black\n"
"\n"
"}\n"
"QPushButton:hover{	\n"
"	\n"
"	color: rgb(255, 255, 255);	\n"
"	background-color: rgb(0, 80, 121);\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_cadastrar_perfil)

        self.label_23 = QLabel(self.pg_cadastro_perfil)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_13.addWidget(self.label_23)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.Pages.addWidget(self.pg_cadastro_perfil)
        self.pg_devteam9 = QWidget()
        self.pg_devteam9.setObjectName(u"pg_devteam9")
        self.label_15 = QLabel(self.pg_devteam9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 9, 731, 52))
        self.label_15.setFont(font1)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_20 = QLabel(self.pg_devteam9)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(70, 90, 621, 341))
        font3 = QFont()
        font3.setPointSize(14)
        self.label_20.setFont(font3)
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_20.setWordWrap(True)
        self.Pages.addWidget(self.pg_devteam9)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.label_16 = QLabel(self.pg_sobre)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 10, 721, 52))
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_19 = QLabel(self.pg_sobre)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(210, 80, 341, 391))
        self.label_19.setFont(font3)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setWordWrap(True)
        self.Pages.addWidget(self.pg_sobre)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_3 = QVBoxLayout(self.pg_home)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(36, 31, 175);")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_pg_cadastrar_sistema = QPushButton(self.pg_home)
        self.btn_pg_cadastrar_sistema.setObjectName(u"btn_pg_cadastrar_sistema")
        self.btn_pg_cadastrar_sistema.setMinimumSize(QSize(148, 30))
        self.btn_pg_cadastrar_sistema.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_cadastrar_sistema.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius: 8px;\n"
"	font-size: 16px;	\n"
"	background-color: #fff;\n"
"	color: black\n"
"\n"
"}\n"
"QPushButton:hover{	\n"
"	\n"
"	color: rgb(255, 255, 255);	\n"
"	background-color: rgb(0, 80, 121);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_pg_cadastrar_sistema)

        self.btn_pg_cadastrar_perfil = QPushButton(self.pg_home)
        self.btn_pg_cadastrar_perfil.setObjectName(u"btn_pg_cadastrar_perfil")
        self.btn_pg_cadastrar_perfil.setMinimumSize(QSize(148, 30))
        self.btn_pg_cadastrar_perfil.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_cadastrar_perfil.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius: 8px;\n"
"	font-size: 16px;	\n"
"	background-color: #fff;\n"
"	color: black\n"
"\n"
"}\n"
"QPushButton:hover{	\n"
"	\n"
"	color: rgb(255, 255, 255);	\n"
"	background-color: rgb(0, 80, 121);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_pg_cadastrar_perfil)

        self.btn_pg_cadastro_usuario = QPushButton(self.pg_home)
        self.btn_pg_cadastro_usuario.setObjectName(u"btn_pg_cadastro_usuario")
        self.btn_pg_cadastro_usuario.setMinimumSize(QSize(148, 30))
        self.btn_pg_cadastro_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_cadastro_usuario.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius: 8px;\n"
"	font-size: 16px;	\n"
"	background-color: #fff;\n"
"	color: black\n"
"\n"
"}\n"
"QPushButton:hover{	\n"
"	\n"
"	color: rgb(255, 255, 255);	\n"
"	background-color: rgb(0, 80, 121);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_pg_cadastro_usuario)

        self.btn_pg_cadastrar_matriz = QPushButton(self.pg_home)
        self.btn_pg_cadastrar_matriz.setObjectName(u"btn_pg_cadastrar_matriz")
        self.btn_pg_cadastrar_matriz.setMinimumSize(QSize(148, 30))
        self.btn_pg_cadastrar_matriz.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_cadastrar_matriz.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius: 8px;\n"
"	font-size: 16px;	\n"
"	background-color: #fff;\n"
"	color: black\n"
"\n"
"}\n"
"QPushButton:hover{	\n"
"	\n"
"	color: rgb(255, 255, 255);	\n"
"	background-color: rgb(0, 80, 121);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_pg_cadastrar_matriz)

        self.btn_pg_consulta = QPushButton(self.pg_home)
        self.btn_pg_consulta.setObjectName(u"btn_pg_consulta")
        self.btn_pg_consulta.setMinimumSize(QSize(148, 30))
        self.btn_pg_consulta.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_consulta.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius: 8px;\n"
"	font-size: 16px;	\n"
"	background-color: #fff;\n"
"	color: black\n"
"\n"
"}\n"
"QPushButton:hover{	\n"
"	\n"
"	color: rgb(255, 255, 255);	\n"
"	background-color: rgb(0, 80, 121);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_pg_consulta)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.Pages.addWidget(self.pg_home)
        self.pg_consultas = QWidget()
        self.pg_consultas.setObjectName(u"pg_consultas")
        self.Pages.addWidget(self.pg_consultas)
        self.pg_cadastro_matriz = QWidget()
        self.pg_cadastro_matriz.setObjectName(u"pg_cadastro_matriz")
        self.verticalLayout_5 = QVBoxLayout(self.pg_cadastro_matriz)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_21 = QLabel(self.pg_cadastro_matriz)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_21)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.pg_cadastro_matriz)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.cb_cod_sys_01 = QComboBox(self.pg_cadastro_matriz)
        self.cb_cod_sys_01.setObjectName(u"cb_cod_sys_01")
        self.cb_cod_sys_01.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.cb_cod_sys_01)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.pg_cadastro_matriz)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.cb_nome_perfil_01 = QComboBox(self.pg_cadastro_matriz)
        self.cb_nome_perfil_01.setObjectName(u"cb_nome_perfil_01")
        self.cb_nome_perfil_01.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.cb_nome_perfil_01)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.pg_cadastro_matriz)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.cb_cod_sys_02 = QComboBox(self.pg_cadastro_matriz)
        self.cb_cod_sys_02.setObjectName(u"cb_cod_sys_02")
        self.cb_cod_sys_02.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.cb_cod_sys_02)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.pg_cadastro_matriz)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.cb_nome_perfil_02 = QComboBox(self.pg_cadastro_matriz)
        self.cb_nome_perfil_02.setObjectName(u"cb_nome_perfil_02")
        self.cb_nome_perfil_02.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.cb_nome_perfil_02)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.tb_cad_sod = QTableView(self.pg_cadastro_matriz)
        self.tb_cad_sod.setObjectName(u"tb_cad_sod")

        self.verticalLayout_5.addWidget(self.tb_cad_sod)

        self.Pages.addWidget(self.pg_cadastro_matriz)

        self.verticalLayout_17.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_pg_consulta_2.setText(QCoreApplication.translate("MainWindow", u"CONSULTAS", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"TABLES", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.btn_devteam9.setText(QCoreApplication.translate("MainWindow", u"DEV TEAM 09", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Tabela</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Cadastro de Sistemas</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Sistema: </span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Descri\u00e7\u00e3o:</span></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">C\u00f3digo:</span></p></body></html>", None))
        self.label_32.setText("")
        self.btn_cadastrar_sistema.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_33.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Cadastrar Usu\u00e1rio</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">CPF:      </span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Nome:      </span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Senha:  </span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Senha:  </span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Sistema:    </span></p></body></html>", None))
        self.cb_sistema_usuario.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_sistema_usuario.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Perfil:    </span></p></body></html>", None))
        self.cb_perfil_usuario.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil_usuario.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Access: </span></p></body></html>", None))
        self.cb_access_usuario.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_access_usuario.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_12.setText("")
        self.btn_cadastrar_usuario.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_13.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Cadastro Perfil de Acesso</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Perfil: </span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Descri\u00e7\u00e3o:</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">C\u00f3digo:</span></p></body></html>", None))
        self.label_22.setText("")
        self.btn_cadastrar_perfil.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_23.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Grupo Miss\u00e3o Certifica\u00e7\u00e3o </span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Mundo 1 Turma 2023.2</span></p><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">DEV TEAM 09</span><span style=\" color:#ffffff;\"><br/></span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">RUY ALEXANDRE DE OLIVEIRA ARAU... -202211644306@alunos.estacio.br </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">TH\u00c9O LOMEU BRAGA ----------------------202306174781@alunos.estacio.br </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">WENDEL FERREIRA COELHO --------------202304676186@alunos.estacio.br </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">FRANCISCO CLAUDIO DE ASSIS OLI.. ----202305260153@alunos.estacio.br </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">GUSTAVO I"
                        "GOR DA SILVA -----------------202305342613@alunos.estacio.br </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">ANDRE LUIZ SANTOS BARROSO ----------202306348682@alunos.estacio.br </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">SALOM\u00c3O ISAAC CARVALHO GARCIA ---202306151251@alunos.estacio.br</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Tela de Sobre</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Desenvolver uma</span></p><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">aplica\u00e7\u00e3o para</span></p><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">gerenciamento da matriz</span></p><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">de Segrega\u00e7\u00e3o de</span></p><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Fun\u00e7\u00f5es que em ingl\u00eas</span></p><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">chama-se \u201cSegregation</span></p><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">of Duties\u201d (SoD)</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#000062;\">SYS-SOD</span></p><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#000062;\">Sistema de </span></p><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#000062;\">Gerenciamento</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">SYS-SOD</span></p><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#ffffff;\">Sistema de Gerenciamento</span></p><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#ffffff;\"><img src=\"imgs/logoe.png\"</span></p></body></html>", None))
        self.btn_pg_cadastrar_sistema.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Sistema", None))
        self.btn_pg_cadastrar_perfil.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Perfil", None))
        self.btn_pg_cadastro_usuario.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.btn_pg_cadastrar_matriz.setText(QCoreApplication.translate("MainWindow", u"Cadastrar de Matriz", None))
        self.btn_pg_consulta.setText(QCoreApplication.translate("MainWindow", u"Consultas", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Cadastro Matriz SoD</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">C\u00f3digo Sistema 1</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Nome do Perfil 1</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">C\u00f3digo Sistema 2</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Nome do Perfil 2</span></p></body></html>", None))
    # retranslateUi


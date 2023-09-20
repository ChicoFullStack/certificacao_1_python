from PySide6.QtCore import*
from PySide6.QtGui import*

class CustomTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)

        self.meus_dados = data[0]
        self.minhas_colunas = data[1]

        self.load_data(self.meus_dados)

    def load_data(self, dados):
        self.numero_linhas = len(dados)
        self.numero_colunas = len(dados[0])


    def rowCount(self, parent=QModelIndex()):
        return self.numero_linhas

    def columnCount(self, parent=QModelIndex()):
        return self.numero_colunas
    
    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self.minhas_colunas[section].upper()
        else:
            return section

    def data(self, index, role=Qt.DisplayRole):
        column = index.column()
        row = index.row()

        if role == Qt.DisplayRole:
            return self.meus_dados[row][column]
        elif role == Qt.TextAlignmentRole:
            if column == 0 or column == 1 or column == 4:
                return Qt.AlignCenter
            return Qt.AlignLeft
        elif role == Qt.BackgroundRole:
            if column == 0:
                return QColor(Qt.lightGray)
            return QColor(Qt.white)
        
        return None

    
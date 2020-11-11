import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel
from AffineCypherDA import AffineCypher
from CeasarCypherDA import CeasarCypher
from RailFence import RailFence
from Inverse import Inverse
from RSA import RSA

class Cypher(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.CC = QPushButton("Ceasar Cypher", self)
        self.AC = QPushButton("Affine Cypher", self)
        self.RF = QPushButton("Rail Fence", self)
        self.Inv = QPushButton("Inverse", self)
        self.RSA = QPushButton("RSA", self)

        self.CC.move(10, 10)
        self.AC.move(10, 50)
        self.RF.move(10, 90)
        self.Inv.move(10, 130)
        self.RSA.move(10,170)

        self.CC.clicked.connect(self.CypherWindow)
        self.AC.clicked.connect(self.AffineWindow)
        self.RF.clicked.connect(self.RailWindow)
        self.Inv.clicked.connect(self.InvWindow)
        self.RSA.clicked.connect(self.RSAWindow)

        self.setGeometry(150, 150, 150, 210)
        self.setWindowTitle("Available Cyphers")
        self.show()

    def CypherWindow(self):
        self.obj1 = CeasarCypher()
    def AffineWindow(self):
        self.obj1 = AffineCypher()
    def RailWindow(self):
        self.obj1 = RailFence()
    def InvWindow(self):
        self.obj1 = Inverse()
    def RSAWindow(self):
        self.obj1 = RSA()
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    obj = Cypher()
    sys.exit(app.exec_())
    

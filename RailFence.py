import numpy as np
import itertools as it
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
import sys

class RailFence(QWidget):

    cypherText = ""
    key = 0

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.title = QLabel("RAIL FENCE CYPHER", self)
        self.title.move(60, 5)
        self.title.setFont(QFont('TimesRoman',10))
        
        self.plainEdit = QLineEdit(self)
        self.plainEdit.setPlaceholderText("Enter a Message")
        self.plainEdit.move(60, 40)

        self.keyEdit = QLineEdit(self)
        self.keyEdit.setPlaceholderText("Enter a Key")
        self.keyEdit.move(250, 40)

        self.lbl = QLabel(self)
        self.lbl.move(60, 100)
        self.lbl.setText("Wait for the Message")
        
        self.encrypt = QPushButton("Encrypt", self)
        self.encrypt.move(60, 160)

        self.decrypt = QPushButton("Decrypt", self)
        self.decrypt.move(250, 160)

        self.encrypt.clicked.connect(self.encryptFun)
        self.decrypt.clicked.connect(self.decryptFun)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("Rail Fence")
        self.show()

    def encryptFun(self):
        
        #Rail Fence Encryption 
        RailFence.key = int(self.keyEdit.text())
        plainText = str(self.plainEdit.text()).replace(" ","")
        arr = np.empty((RailFence.key,len(plainText)), dtype=str)     #Creating an Empty array
        x = 0
        for i in range(len(plainText)):
            if x == (len(plainText)):break
            else:
                for j in it.chain(range(0,RailFence.key,1), range(RailFence.key-2,0,-1)):
                    if x == len(plainText):break
                    arr[j][x] = plainText[x]
                    x += 1
        RailFence.cypherText = "".join(it.chain(*arr.tolist()))
        self.lbl.setText("Encrypted Message is --> "+RailFence.cypherText)
        self.lbl.adjustSize()

    def decryptFun(self):
        #Rail Fence Decryption
        x = 0
        arr = np.empty((RailFence.key, len(RailFence.cypherText)), dtype=str)
        for i in range(len(RailFence.cypherText)):
            if x == len(RailFence.cypherText):break
            else:
                for j in it.chain(range(0,RailFence.key,1), range((RailFence.key)-2,0,-1)):
                    if x == len(RailFence.cypherText):break
                    arr[j][x] = "*"
                    x += 1
        x = 0
        for i in range(RailFence.key):
            for j in range(len(RailFence.cypherText)):
                if arr[i][j] == "*":
                    arr[i][j] = RailFence.cypherText[x]
                    x += 1
                else:continue
        self.lbl.setText("Decrypt Message is --> "+"".join(it.chain(*(arr.T).tolist())))
        self.lbl.adjustSize()
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    obj = RailFence()
    sys.exit(app.exec_())
    

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QFont

class CeasarCypher(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.cypherText = ""
        self.alphaLower = 'abcdefghijklmnopqrstuwxyz'
        self.alphaUpper = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'

        self.title = QLabel("CEASAR CYPHER", self)
        self.title.move(60, 5)
        self.title.setFont(QFont('TimesRoman',10))

        self.edit = QLineEdit(self)
        self.edit.setPlaceholderText("Enter a Message")
        self.edit.move(60, 40)

        self.k = QLineEdit(self)
        self.k.setPlaceholderText("Enter a Key")
        self.k.move(250, 40)

        self.cypherLabel = QLabel("Wait for the Message???",self)
        self.cypherLabel.move(60, 100)

        encrypt = QPushButton("Encrypt", self)
        encrypt.move(60, 160)

        decrypt = QPushButton("Decrypt", self)
        decrypt.move(250, 160)

        encrypt.clicked.connect(self.encryptFun)
        decrypt.clicked.connect(self.decryptFun)
       
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("Ceasar Cypher")
        self.show()

    def encryptFun(self):

        self.cypherText = " "
        plainText = self.edit.text()
        key = int(self.k.text())
        for i in plainText:
            if i in self.alphaLower:
                self.cypherText += self.alphaLower[(self.alphaLower.index(i) + key)%len(self.alphaLower)]
    
            if i in self.alphaUpper:
                self.cypherText += self.alphaUpper[(self.alphaUpper.index(i) + key)%len(self.alphaUpper)]

            if i == " ":
                self.cypherText += " "
        self.cypherLabel.setText(self.cypherText)
        self.cypherLabel.adjustSize()

    def decryptFun(self):

        x = ""
        key = int(self.k.text())
        for i in self.cypherText:
            if i in self.alphaLower:
                x += self.alphaLower[(self.alphaLower.index(i) - key)%len(self.alphaLower)]
    
            if i in self.alphaUpper:
                x += self.alphaUpper[(self.alphaUpper.index(i) - key)%len(self.alphaUpper)]

            if i == " ":
                x += " "
        self.cypherLabel.setText(x)
        self.cypherLabel.adjustSize()        
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    obj = CeasarCypher()
    sys.exit(app.exec_())

        

        

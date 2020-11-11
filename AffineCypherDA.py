import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QFont

class AffineCypher(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.title = QLabel("AFFINE CYPHER", self)
        self.title.move(60, 5)
        self.title.setFont(QFont('TimesRoman',10))

        self.edit = QLineEdit(self)
        self.edit.setPlaceholderText("Enter a Message")
        self.edit.move(60, 40)

        self.ka = QLineEdit(self)
        self.ka.setPlaceholderText("Enter a Key A")
        self.ka.move(250, 40)

        self.kb = QLineEdit(self)
        self.kb.setPlaceholderText("Enter a Key B")
        self.kb.move(440, 40)

        self.cypherLabel = QLabel("Encrypted Message???",self)
        self.cypherLabel.move(60, 100)

        encrypt = QPushButton("Encrypt", self)
        encrypt.move(60, 160)

        encrypt.clicked.connect(self.encryptFun)

        self.setGeometry(300, 300, 650, 300)
        self.setWindowTitle("Affine Cypher")
        self.show()

    def encryptFun(self):

        alphaLower = 'abcdefghijklmnopqrstuwxyz'
        alphaUpper = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'
        cypherText = ""
        plainText = self.edit.text()
        for i in plainText:
            if i in alphaLower:
                cypherText += alphaLower[((alphaLower.index(i)*int(self.ka.text())) + int(self.kb.text()))%len(alphaLower)]
    
            if i in alphaUpper:
                cypherText += alphaUpper[((alphaUpper.index(i)*int(self.ka.text())) + int(self.kb.text()))%len(alphaUpper)]

            if i == " ":
                cypherText += " "
        self.cypherLabel.setText(cypherText)
        self.cypherLabel.adjustSize()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    obj = AffineCypher()
    sys.exit(app.exec_())

        

        

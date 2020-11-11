import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QFont
from decimal import Decimal

class RSA(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.ct = 0
        self.d = 0
        self.n = 0

        self.title = QLabel("RSA", self)
        self.title.move(60, 5)
        self.title.setFont(QFont('TimesRoman',10))

        self.edit = QLineEdit(self)
        self.edit.setPlaceholderText("Enter a Message")
        self.edit.move(60, 40)

        self.a = QLineEdit(self)
        self.a.setPlaceholderText("Enter a 1st PrimeNo.")
        self.a.move(250, 40)

        self.b = QLineEdit(self)
        self.b.setPlaceholderText("Enter a 2nd PrimeNo.")
        self.b.move(440, 40)

        self.lbl = QLabel(self)
        self.lbl.move(60, 100)
        self.lbl.setText("Wait for the Message")
        
        self.encrypt = QPushButton("Encrypt", self)
        self.encrypt.move(60, 160)

        self.decrypt = QPushButton("Decrypt", self)
        self.decrypt.move(250, 160)

        self.encrypt.clicked.connect(self.encryptFun)
        self.decrypt.clicked.connect(self.decryptFun)

        self.setGeometry(300, 300, 600, 300)
        self.setWindowTitle("RSA")
        self.show()

    def encryptFun(self):
        def gcd(e,t): 
            if t==0: 
                return e
            else: 
                return gcd(t,e%t)

        a1 = int(self.a.text())
        b1 = int(self.b.text())
        text = self.edit.text()
        text = text.lower()
        output = []
        for character in text:
            number = ord(character) - 96
            output.append(str(number))
        ind = int(''.join(output))

        self.n = a1*b1 
        t = (a1-1)*(b1-1)

        for e in range(2,t): 
            if gcd(e,t)== 1: 
                break


        for i in range(1,10): 
            x = 1 + i*t 
            if x % e == 0: 
                self.d = int(x/e) 
                break
        ctt = Decimal(0) 
        ctt =pow(ind,e) 
        self.ct = ctt % self.n 

        self.lbl.setText("Encrypted Message is "+str(self.ct))
        self.lbl.adjustSize()

    def decryptFun(self):

        dtt = Decimal(0) 
        dtt = pow(self.ct,self.d) 
        dt = dtt % self.n

        self.lbl.setText("Decrypted Message is "+str(dt))
        self.lbl.adjustSize()
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    obj = RSA()
    sys.exit(app.exec_())

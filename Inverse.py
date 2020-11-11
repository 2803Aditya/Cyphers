import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QFont

class Inverse(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.title = QLabel("MULTIPLICATIVE INVERSE", self)
        self.title.move(60, 5)
        self.title.setFont(QFont('TimesRoman',10))

        self.a = QLineEdit(self)
        self.a.setPlaceholderText("Enter value of A")
        self.a.move(60, 40)

        self.m = QLineEdit(self)
        self.m.setPlaceholderText("Enter value of M")
        self.m.move(250, 40)

        self.lbl = QLabel("Result!!!", self)
        self.lbl.move(60, 100)

        btn = QPushButton("Inverse", self)
        btn.move(60, 160)

        btn.clicked.connect(self.inv)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("Multiplicative Inverse")
        self.show()

    def inv(self):
        A = int(self.a.text())
        M = int(self.m.text())
        A = A % M
        for i in range(2, M):
            if ((A*i) % M == 1):
                self.lbl.setText(str(i))
                self.lbl.adjustSize()   
                break
            
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    obj = Inverse()
    sys.exit(app.exec_())

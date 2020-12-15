from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from ui import Ui_MainWindow
from PyQt5 import uic
from random import randint
import sys


class YellowCirlces(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.draw_btn.clicked.connect(self.repaint)

    def draw_rnd_circle(self, qp):
        r = randint(1, 570)
        x = randint(90, 600)
        y = randint(30, 600)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(x, y, r, r)

    def paintEvent(self, event):
        if self.sender() is not None and self.sender().text() == "Draw circles":
            qp = QPainter()
            qp.begin(self)
            self.draw_rnd_circle(qp)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    yc = YellowCirlces()
    yc.show()
    sys.exit(app.exec())

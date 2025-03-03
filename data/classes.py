from PyQt6.QtGui import QPainter, QColor
from forms.Ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow
from random import randint


SIZE = [800, 600]


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.n = randint(10, 20)
        self.flag = False
        self.setWindowTitle('Git и случайные окружности')
        self.btn.clicked.connect(self.draw)


    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.flag:
            for i in range(self.n):
                self.color = (randint(0, 256), randint(0, 256), randint(0, 256))
                qp.setPen(QColor(*self.color))
                qp.setBrush(QColor(*self.color))
                self.x, self.y = randint(50, SIZE[0] - 50), randint(50, SIZE[1] - 50)
                self.size = randint(10, 50)
                qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()
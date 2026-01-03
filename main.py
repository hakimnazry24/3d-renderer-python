from PySide6 import QtWidgets, QtGui
import sys
from draw_line import DrawLine

WIDTH = 800
HEIGHT = 800


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.image = QtGui.QImage(WIDTH, HEIGHT, QtGui.QImage.Format.Format_RGB32)

        draw_line = DrawLine(self.image, WIDTH, HEIGHT, 100, 10, 100)
        draw_line.draw_horizontal_line(100, 10)
        draw_line.draw_vertical_line(100, 10)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(WIDTH, HEIGHT)

        widget = MyWidget()
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())

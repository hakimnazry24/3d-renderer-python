from PySide6 import QtCore, QtWidgets, QtGui
import sys

WIDTH = 800
HEIGHT = 800


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.image = QtGui.QImage(WIDTH, HEIGHT, QtGui.QImage.Format.Format_RGB32)
        color = QtGui.QColor(100, 20, 100)

        self.draw_horizontal_line(100, 10, color)
        self.draw_vertical_line(100, 10, color)
        self.draw_line(0, 0, WIDTH, HEIGHT, 10, color)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)

    def draw_horizontal_line(self, y_start, thick, color):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if y >= y_start and y <= y_start + thick:
                    self.image.setPixelColor(x, y, color)

    def draw_vertical_line(self, x_start, thick, color):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if x >= x_start and x <= x_start + thick:
                    self.image.setPixelColor(x, y, color)

    def draw_line(self, x_start, y_start, x_end, y_end, thickness, color):
        slope = (y_end - y_start) / (x_end - x_start)

        for x in range(WIDTH):
            y = slope * x
            if x >= x_start and x <= x_end:
                if y >= y_start and y <= y_end:
                    self.image.setPixelColor(x, y, color)

                    for i in range(1, thickness):
                        self.image.setPixelColor(x + i, y, color)
                        self.image.setPixelColor(x - i, y, color)


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

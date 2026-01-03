from PySide6.QtGui import QImage, QColor

class DrawLine:
    def __init__(self, image: QImage, WIDTH, HEIGHT, r, g, b):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.image = image
        self.color = QColor(r, g, b)

    def draw_horizontal_line(self, y_start, thick):
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                if y >= y_start and y <= y_start + thick:
                    self.image.setPixelColor(x, y, self.color)

    def draw_vertical_line(self, x_start, thick):
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                if x >= x_start and x <= x_start + thick:
                    self.image.setPixelColor(x, y, self.color)

    def draw_line(self, x_start, y_start, x_end, y_end, thickness):
        slope = (y_end - y_start) / (x_end - x_start)

        for x in range(self.WIDTH):
            y = slope * x
            if x >= x_start and x <= x_end:
                if y >= y_start and y <= y_end:
                    self.image.setPixelColor(x, y, self.color)

                    for i in range(1, thickness):
                        self.image.setPixelColor(x + i, y, self.color)
                        self.image.setPixelColor(x - i, y, self.color)
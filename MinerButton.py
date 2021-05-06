from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, pyqtSlot


class MinerButton(QPushButton):
    def __init__(self, parent_window, x_coord, y_coord):
        super().__init__(parent_window)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.parent_window = parent_window
        self.opened = False
        self.setStyleSheet("background-color: lightblue;")


    def setCoords(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def getCoords(self):
        return self.x_coord, self.y_coord

    def mousePressEvent(self, event) -> None:
        super().mousePressEvent(event)
        if self.opened:
            return
        self.setStyleSheet("background-color: lightgrey;")
        self.parent_window.smileButton.setStyleSheet("background:url(./img/smile2.png) center no-repeat;")

    def mouseReleaseEvent(self, event) -> None:
        super().mouseReleaseEvent(event)
        self.parent_window.smileButton.setStyleSheet("background:url(./img/smile1.png) center no-repeat;")
        if self.opened:
            return

        self.setStyleSheet("background-color: lightblue;")
        self.parent_window.run(self, event.button())

    def disableButton(self):
        self.opened = True
        self.setDisabled(True)

    def setValue(self, value):
        if str(value) == "▣":
            self.setText(" ")
            return

        self.setText(str(value))

        if  str(value) == "🚩":
            return

        self.setStyleSheet("background-color: lightgrey;")

        if str(value) in "0123456789":
            value = int(value)
            r = (100 + value * 321) % 256
            g = (value * 29) % 256
            b = (255 - value * 91) % 256
            self.setStyleSheet(f"background-color: lightgrey;"
                               f"color: rgb({r}, {g}, {b});"
                               f"font-weight: bold;")

            if value == 0:
                self.setText(" ")

            self.disableButton()
            return

    def isOpened(self):
        return self.opened




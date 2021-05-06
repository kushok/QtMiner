import sys, threading

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5 import QtWidgets
from PyQt5 import uic

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMouseEvent

from Settings import Settings
from score import Score
from Game import Game
from MinerButton import MinerButton


class UIGame(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/mainWindow.ui", self)
        self.height, self.width, self.bombs = 10, 10, 10
        self.buttons = []
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 150, 150)
        self.setWindowTitle('Сапёр')
        self.gridLayout.setSpacing(1)

        self.settingsButton.clicked.connect(self.openSettings)
        self.smileButton.clicked.connect(self.repeatGame)
        self.scoreButton.clicked.connect(self.openScore)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timerLooper)
        self.timer.setInterval(1000)
        # self.timer.


        self.openSettings()

    def timerLooper(self):
        sec = int(self.lcdNumber.value())
        self.lcdNumber.display(str(sec + 1))

    def openScore(self):
        settings_dialog = Score()
        settings_dialog.show()
        settings_dialog.exec_()

    def openSettings(self):
        settings_dialog = Settings(self)
        settings_dialog.show()
        settings_dialog.exec_()

    def repeatGame(self):
        self.start(self.height, self.width, self.bombs)

    def start(self, height, width, bombs):
        self.lcdNumber.display("0")
        self.height = height
        self.width = width
        self.bombs = bombs
        self.smileButton.setStyleSheet("background:url(./img/smile1.png) center no-repeat;")
        self.clearLayout(self.gridLayout)

        self.game = Game(height, width, bombs)
        self.buttons.clear()

        for i in range(height):
            self.buttons.append([])
            for j in range(width):
                button = MinerButton(self, i, j)
                button.setText(" ")
                button.setCoords(i, j)

                button.setMinimumSize(15, 15)
                button.setMaximumSize(600, 600)

                self.gridLayout.addWidget(button, i, j)
                self.buttons[i].append(button)

    def run(self, sender, button):
        if not self.timer.isActive():
            self.timer.start()

        x, y = sender.getCoords()
        if button == Qt.LeftButton:
            status = self.game.doStep(x, y)
        elif button == Qt.RightButton:
            self.game.changeFlag(x, y)
            self.updateField()
            return
        self.updateField()

        if status == Game.WIN:
            self.timer.stop()
            self.smileButton.setStyleSheet("background:url(./img/smile3.png) center no-repeat;")
            time = int(self.lcdNumber.value())

            level = 0
            if (self.height, self.width, self.bombs) == (10, 10, 10):
                Score().setMaxScore(Score.EASY, time)
            elif (self.height, self.width, self.bombs) == (16, 16, 40):
                Score().setMaxScore(Score.MEDIUM, time)
            elif (self.height, self.width, self.bombs) == (30, 16, 99):
                Score().setMaxScore(Score.PRO, time)

            self.disableButtons()
            return

        if status == Game.LOSE:
            self.timer.stop()
            self.smileButton.setStyleSheet("background:url(./img/smile4.png) center no-repeat;")
            self.disableButtons()

    def disableButtons(self):
        for i in range(self.height):
            for j in range(self.width):
                self.buttons[i][j].setDisabled(True)


    def updateField(self):
        field = self.game.getGameField()
        # print(self.game)

        for i in range(self.game.getHeight()):
            for j in range(self.game.getWidth()):
                # if self.buttons[i][j].isOpened:
                #    continue
                self.buttons[i][j].setValue(field[i][j])

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()


def my_exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


if __name__ == '__main__':
    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook

    app = QApplication(sys.argv)
    ex = UIGame()
    ex.show()
    sys.exit(app.exec_())

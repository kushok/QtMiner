from ui.ui_settings import Ui_Dialog  # Импортируем uic
from PyQt5.QtWidgets import QDialog


class Settings(QDialog, Ui_Dialog):
    def __init__(self, parentWindow):
        QDialog.__init__(self)
        self.setupUi(self)
        self.parentWindow = parentWindow

        self.buttonBox.accepted.connect(self.accept_data)
        self.buttonBox.rejected.connect(self.reject_data)

        self.buttonGroup.buttonClicked.connect(self.radioChanged)

    def radioChanged(self, sender):
        inputs = [self.widthInput, self.heightInput, self.bombsInput]

        if sender == self.otherRadio:
            for inputQt in inputs:
                inputQt.setEnabled(True)
                inputQt.setStyleSheet("background: #FFF")
            return
        else:
            for inputQt in inputs:
                inputQt.setEnabled(False)
                inputQt.setStyleSheet("background: #DDDDFF")

        if sender == self.easyRadio:
            self.widthInput.setValue(10)
            self.heightInput.setValue(10)
            self.bombsInput.setValue(10)
        elif sender == self.mediumRadio:
            self.widthInput.setValue(16)
            self.heightInput.setValue(16)
            self.bombsInput.setValue(40)
        elif sender == self.proRadio:
            self.widthInput.setValue(30)
            self.heightInput.setValue(16)
            self.bombsInput.setValue(99)

    def accept_data(self):
        self.parentWindow.start(*map(int, [self.heightInput.value(), self.widthInput.value(), self.bombsInput.value()]))
        # print("accept")
        self.close()

    def reject_data(self) -> None:
        # print("reject")
        self.close()

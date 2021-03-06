# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(400, 260)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background: #DDDDFF")
        Dialog.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 200, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 19, 361, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.easyRadio = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.easyRadio.setAutoFillBackground(True)
        self.easyRadio.setChecked(True)
        self.easyRadio.setObjectName("easyRadio")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.easyRadio)
        self.verticalLayout_5.addWidget(self.easyRadio)
        self.mediumRadio = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.mediumRadio.setAutoFillBackground(True)
        self.mediumRadio.setObjectName("mediumRadio")
        self.buttonGroup.addButton(self.mediumRadio)
        self.verticalLayout_5.addWidget(self.mediumRadio)
        self.proRadio = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.proRadio.setObjectName("proRadio")
        self.buttonGroup.addButton(self.proRadio)
        self.verticalLayout_5.addWidget(self.proRadio)
        self.otherRadio = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.otherRadio.setObjectName("otherRadio")
        self.buttonGroup.addButton(self.otherRadio)
        self.verticalLayout_5.addWidget(self.otherRadio)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, 50, -1, 40)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widthLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.widthLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.widthLabel.setObjectName("widthLabel")
        self.verticalLayout_8.addWidget(self.widthLabel)
        self.widthInput = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.widthInput.setEnabled(False)
        self.widthInput.setProperty("value", 10)
        self.widthInput.setObjectName("widthInput")
        self.verticalLayout_8.addWidget(self.widthInput)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, 50, -1, 40)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setEnabled(True)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.heightInput = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.heightInput.setEnabled(False)
        self.heightInput.setProperty("value", 10)
        self.heightInput.setObjectName("heightInput")
        self.verticalLayout_7.addWidget(self.heightInput)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 50, -1, 40)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.bombsInput = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.bombsInput.setEnabled(False)
        self.bombsInput.setProperty("value", 10)
        self.bombsInput.setObjectName("bombsInput")
        self.verticalLayout_4.addWidget(self.bombsInput)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "??????????????????"))
        self.easyRadio.setText(_translate("Dialog", "??????????????"))
        self.mediumRadio.setText(_translate("Dialog", "????????????????"))
        self.proRadio.setText(_translate("Dialog", "????????????????????????"))
        self.otherRadio.setText(_translate("Dialog", "????????????"))
        self.widthLabel.setText(_translate("Dialog", "????????????"))
        self.label.setText(_translate("Dialog", "????????????"))
        self.label_2.setText(_translate("Dialog", "????????????????????\n"
"????????"))

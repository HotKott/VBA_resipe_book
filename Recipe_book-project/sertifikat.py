# Form implementation generated from reading ui file 'sertifikat.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import defs

class Ui_sertifikat(object):
    def setupUi(self, sertifikat):
        sertifikat.setObjectName("sertifikat")
        sertifikat.resize(726, 470)
        sertifikat.setMaximumSize(QtCore.QSize(726, 470))
        font = QtGui.QFont()
        font.setPointSize(12)
        sertifikat.setFont(font)
        sertifikat.setStyleSheet("background-color: rgb(218,236,255);")
        self.centralwidget = QtWidgets.QWidget(parent=sertifikat)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(235, 260, 250, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(726, 470))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(136,155,211);")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(210, 190, 301, 41))
        self.textEdit.setMaximumSize(QtCore.QSize(726, 470))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(246,250,255); ")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 130, 441, 31))
        self.label.setMaximumSize(QtCore.QSize(726, 470))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 390, 150, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(726, 470))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(136,155,211);")
        self.pushButton_2.setObjectName("pushButton_2")
        sertifikat.setCentralWidget(self.centralwidget)


        self.pushButton_2.clicked.connect(lambda: defs.go_to_new_file("profile_Ui.py"))
        self.pushButton.clicked.connect(lambda: defs.Sertifikat(self.textEdit.toPlainText()))


        self.retranslateUi(sertifikat)
        QtCore.QMetaObject.connectSlotsByName(sertifikat)

    def retranslateUi(self, sertifikat):
        _translate = QtCore.QCoreApplication.translate
        sertifikat.setWindowTitle(_translate("sertifikat", "MainWindow"))
        self.pushButton.setText(_translate("sertifikat", "Получить сертификат"))
        self.label.setText(_translate("sertifikat", "Введите ваше имя для получения сертификата"))
        self.pushButton_2.setText(_translate("sertifikat", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sertifikat = QtWidgets.QMainWindow()
    ui = Ui_sertifikat()
    ui.setupUi(sertifikat)
    sertifikat.show()
    sys.exit(app.exec())

# Form implementation generated from reading ui file 'poisk.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import defs

class Ui_Poisk(object):
    def setupUi(self, Poisk):
        Poisk.setObjectName("Poisk")
        Poisk.resize(800, 513)
        Poisk.setMaximumSize(QtCore.QSize(800, 513))
        Poisk.setStyleSheet("background-color: rgb(218,236,255);")
        self.poisk = QtWidgets.QWidget(parent=Poisk)
        self.poisk.setObjectName("poisk")
        self.pushButton = QtWidgets.QPushButton(parent=self.poisk)
        self.pushButton.setGeometry(QtCore.QRect(500, 180, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(136,155,211); ")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.poisk)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 340, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(136,155,211); ")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(parent=self.poisk)
        self.textEdit.setGeometry(QtCore.QRect(60, 180, 381, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(246,250,255);")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(parent=self.poisk)
        self.label.setGeometry(QtCore.QRect(310, 50, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.poisk)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.poisk)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 260, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(136,155,211); ")
        self.pushButton_3.setObjectName("pushButton_3")
        Poisk.setCentralWidget(self.poisk)
        

        self.pushButton.clicked.connect(lambda: defs.go_to_podbor("podbor_Ui.py",self.textEdit.toPlainText()))
        self.pushButton_2.clicked.connect(lambda: defs.go_to_new_file("GL_Ui.py"))
        self.pushButton_3.clicked.connect(self.textEdit.clear)


        self.retranslateUi(Poisk)
        QtCore.QMetaObject.connectSlotsByName(Poisk)

    def retranslateUi(self, Poisk):
        _translate = QtCore.QCoreApplication.translate
        Poisk.setWindowTitle(_translate("Poisk", "MainWindow"))
        self.pushButton.setText(_translate("Poisk", "Найти рецепты"))
        self.pushButton_2.setText(_translate("Poisk", "На главную"))
        self.label.setText(_translate("Poisk", "Поиск рецепта"))
        self.label_2.setText(_translate("Poisk", "Введите продукты"))
        self.pushButton_3.setText(_translate("Poisk", "Очистить поле ввода"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Poisk = QtWidgets.QMainWindow()
    ui = Ui_Poisk()
    ui.setupUi(Poisk)
    Poisk.show()
    sys.exit(app.exec())
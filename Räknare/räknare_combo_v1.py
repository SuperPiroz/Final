
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 616)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        
        self.SjuButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("7"))
        self.SjuButton.setGeometry(QtCore.QRect(30, 130, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.SjuButton.setFont(font)
        self.SjuButton.setObjectName("SjuButton")
       
        self.attaButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("8"))
        self.attaButton.setGeometry(QtCore.QRect(120, 130, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.attaButton.setFont(font)
        self.attaButton.setObjectName("attaButton")
        
        self.divisionButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("÷"))
        self.divisionButton.setGeometry(QtCore.QRect(300, 130, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divisionButton.setFont(font)
        self.divisionButton.setObjectName("divisionButton")
        
        self.nioButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("9"))
        self.nioButton.setGeometry(QtCore.QRect(210, 130, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nioButton.setFont(font)
        self.nioButton.setObjectName("nioButton")
        
        self.fyraButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("4"))
        self.fyraButton.setGeometry(QtCore.QRect(30, 220, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fyraButton.setFont(font)
        self.fyraButton.setObjectName("fyraButton")
        
        self.multi_pButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("X"))
        self.multi_pButton.setGeometry(QtCore.QRect(300, 220, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multi_pButton.setFont(font)
        self.multi_pButton.setObjectName("multi_pButton")
        
        self.femButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("5"))
        self.femButton.setGeometry(QtCore.QRect(120, 220, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.femButton.setFont(font)
        self.femButton.setObjectName("femButton")
        
        self.sexButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("6"))
        self.sexButton.setGeometry(QtCore.QRect(210, 220, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sexButton.setFont(font)
        self.sexButton.setObjectName("sexButton")
        
        self.treButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("3"))
        self.treButton.setGeometry(QtCore.QRect(30, 310, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.treButton.setFont(font)
        self.treButton.setObjectName("treButton")
       
        self.subtraktionButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("-"))
        self.subtraktionButton.setGeometry(QtCore.QRect(300, 310, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.subtraktionButton.setFont(font)
        self.subtraktionButton.setObjectName("subtraktionButton")
        
        self.tvaButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("2"))
        self.tvaButton.setGeometry(QtCore.QRect(120, 310, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.tvaButton.setFont(font)
        self.tvaButton.setObjectName("tvaButton")
        
        self.ettButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("1"))
        self.ettButton.setGeometry(QtCore.QRect(210, 310, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.ettButton.setFont(font)
        self.ettButton.setObjectName("ettButton")
        
        self.aditionButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("+"))
        self.aditionButton.setGeometry(QtCore.QRect(300, 400, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.aditionButton.setFont(font)
        self.aditionButton.setObjectName("aditionButton")
        
        self.likamedButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("="))
        self.likamedButton.setGeometry(QtCore.QRect(210, 400, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.likamedButton.setFont(font)
        self.likamedButton.setObjectName("likamedButton")
       
        self.nollButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("0"))
        self.nollButton.setGeometry(QtCore.QRect(30, 400, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nollButton.setFont(font)
        self.nollButton.setObjectName("nollButton")
       
        self.komaButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("."))
        self.komaButton.setGeometry(QtCore.QRect(120, 400, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.komaButton.setFont(font)
        self.komaButton.setObjectName("komaButton")
       
        self.clearButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("C"))
        self.clearButton.setGeometry(QtCore.QRect(30, 490, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 401, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def press_it (self, pressed):
        if pressed == "C":
            self.label.setText("0")
        else:
            # Kollar om det börjar på 0 och tar bort 0 isf
            if self.label.text() == "0":
                self.label.setText("")
                # Annars konkatinerar den den tryckta knappen med det som var där innan
            self.label.setText (f'{self.label.text()}{pressed}')
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mini Räknare"))
        self.label.setText(_translate("MainWindow", "0"))
        self.SjuButton.setText(_translate("MainWindow", "7"))
        self.attaButton.setText(_translate("MainWindow", "8"))
        self.divisionButton.setText(_translate("MainWindow", "÷"))
        self.nioButton.setText(_translate("MainWindow", "9"))
        self.fyraButton.setText(_translate("MainWindow", "4"))
        self.multi_pButton.setText(_translate("MainWindow", "X"))
        self.femButton.setText(_translate("MainWindow", "5"))
        self.sexButton.setText(_translate("MainWindow", "6"))
        self.treButton.setText(_translate("MainWindow", "3"))
        self.subtraktionButton.setText(_translate("MainWindow", "-"))
        self.tvaButton.setText(_translate("MainWindow", "2"))
        self.ettButton.setText(_translate("MainWindow", "1"))
        self.aditionButton.setText(_translate("MainWindow", "+"))
        self.likamedButton.setText(_translate("MainWindow", "="))
        self.nollButton.setText(_translate("MainWindow", "0"))
        self.komaButton.setText(_translate("MainWindow", "."))
        self.clearButton.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

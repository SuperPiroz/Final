from PyQt5 import QtCore, QtGui, QtWidgets

                        # Förklaraing i stora drag:

# Geometri: Layouten för knapparna och displayens positoner sätts med setGeometry

# Signal Handling: knapparna triggar press:it funktioen när dom clickas. den här 
# funktionen tar hand om när dom olika knapparna är "pressed" (number appending, 
# operations, etc.)

# Main class (Ui_MainWindow):
# Den här klassen skaper och sätter upp hela GUI genom PyQt5. Den skapar ett fönster(MainWindow)
# med ett rutnät av knappar och en räknar display.


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 616)
        # Huvud fönstret
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Räknarens display
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        
        # Knappen 7
        self.SjuButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("7"))
        self.SjuButton.setGeometry(QtCore.QRect(30, 130, 75, 75)) # Placering
        font = QtGui.QFont()
        font.setPointSize(26)# font storlek
        self.SjuButton.setFont(font)
        self.SjuButton.setObjectName("SjuButton")
        
        # Knappen 8
        self.attaButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("8"))
        self.attaButton.setGeometry(QtCore.QRect(120, 130, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.attaButton.setFont(font)
        self.attaButton.setObjectName("attaButton")
                
        # Knappen ÷
        self.divisionButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("÷"))
        self.divisionButton.setGeometry(QtCore.QRect(300, 130, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divisionButton.setFont(font)
        self.divisionButton.setObjectName("divisionButton")
        
        # Knappen 9
        self.nioButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("9"))
        self.nioButton.setGeometry(QtCore.QRect(210, 130, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nioButton.setFont(font)
        self.nioButton.setObjectName("nioButton")
        
        # Knappen 4
        self.fyraButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("4"))
        self.fyraButton.setGeometry(QtCore.QRect(30, 220, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fyraButton.setFont(font)
        self.fyraButton.setObjectName("fyraButton")
        
        # Knappen X (miltiplikation)
        self.multi_pButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("*"))
        self.multi_pButton.setGeometry(QtCore.QRect(300, 220, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multi_pButton.setFont(font)
        self.multi_pButton.setObjectName("multi_pButton")
        
        # Knappen 5
        self.femButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("5"))
        self.femButton.setGeometry(QtCore.QRect(120, 220, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.femButton.setFont(font)
        self.femButton.setObjectName("femButton")
        
        # Knappen 6
        self.sexButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("6"))
        self.sexButton.setGeometry(QtCore.QRect(210, 220, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sexButton.setFont(font)
        self.sexButton.setObjectName("sexButton")
        
        # Knappen 3
        self.treButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("3"))
        self.treButton.setGeometry(QtCore.QRect(30, 310, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.treButton.setFont(font)
        self.treButton.setObjectName("treButton")
       
        # Knappen -
        self.subtraktionButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("-"))
        self.subtraktionButton.setGeometry(QtCore.QRect(300, 310, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.subtraktionButton.setFont(font)
        self.subtraktionButton.setObjectName("subtraktionButton")
        
        # Knappen 2 
        self.tvaButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("2"))
        self.tvaButton.setGeometry(QtCore.QRect(120, 310, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.tvaButton.setFont(font)
        self.tvaButton.setObjectName("tvaButton")
        
        # Knappen 1
        self.ettButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("1"))
        self.ettButton.setGeometry(QtCore.QRect(210, 310, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.ettButton.setFont(font)
        self.ettButton.setObjectName("ettButton")
        
        # Knappen +
        self.aditionButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("+"))
        self.aditionButton.setGeometry(QtCore.QRect(300, 400, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.aditionButton.setFont(font)
        self.aditionButton.setObjectName("aditionButton")
        
        # Knappen =
        self.likamedButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.math_it())
        self.likamedButton.setGeometry(QtCore.QRect(210, 400, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.likamedButton.setFont(font)
        self.likamedButton.setObjectName("likamedButton")
       
        # Knappen 0
        self.nollButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("0"))
        self.nollButton.setGeometry(QtCore.QRect(30, 400, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nollButton.setFont(font)
        self.nollButton.setObjectName("nollButton")
       
        # Deciamal . 
        self.komaButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.koma_it())
        self.komaButton.setGeometry(QtCore.QRect(120, 400, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.komaButton.setFont(font)
        self.komaButton.setObjectName("komaButton")
       
        # Clear knappen
        self.clearButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("C"))
        self.clearButton.setGeometry(QtCore.QRect(30, 490, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        
        # Ett rutnät av knappar och en räknar display.
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
    # låt oss räkna
    def math_it(self):
        screen = self.label.text()
        try:
        #här görs matematiken
            answer = eval(screen) #eval i python betyder evaulera den tar 2 siffror och 
                               # fattar vad den ska göra om det finns ett aritmiskt tecken mellan 
        
            self.label.setText(str(answer))
        except:
            self.lable.setText("ERROR")
        
    #funktion för decimal tecken och hur den ska bete sig
    def koma_it(self): # avgör att man inte kan läga in mer än ett decimal tecken
        screen = self.label.text()
        screen [-1] == "." # detta säger till så att man inte kan göra ett deciaml tecken i slutet av en sifra 
        pass 
        if"." in screen:
            pass
        else: 
            self.label.setText(f'{screen}.')

        
    # Den här funktioen uppdaterar displayen (lable) baserad på den tryckda knappen. om (c) alltså 
    # Clear är tryckd så rensas displayen och den återsätts till 0.
    def press_it (self, pressed):
        if pressed == "C":
            self.label.setText("0")
        else:
            # Kollar om det börjar på 0 och tar bort 0 isf
            if self.label.text() == "0":
                self.label.setText("")
                # Annars konkatinerar den den tryckta knappen med det som var där innan
            self.label.setText (f'{self.label.text()}{pressed}')
        
    
    # Den här funktionen sätter text för alla kanppar och säkerställer att rätt tecken visas i displayen.
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

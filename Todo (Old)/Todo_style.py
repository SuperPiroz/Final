#Detta är ett ukast från QT-designer jag gjorde klart min design där för att få en grund i koden sen sparade jag den som en UI fil 
#slutligen konverterade jag UI filen till python kod. Nu ska jag gå vidare med att säta ihop designen med min kod och få det hela 
# att funka. Mycket kommer behöva läggas till och tas bort!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 791)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        self.lagg_till = QtWidgets.QPushButton(self.centralwidget)
        self.lagg_till.setGeometry(QtCore.QRect(50, 160, 91, 41))
        self.lagg_till.setObjectName("lagg_till")
        self.lagg_till_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lagg_till_lineEdit.setGeometry(QtCore.QRect(50, 90, 341, 51))
        self.lagg_till_lineEdit.setObjectName("lagg_till_lineEdit")

        self.lista_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.lista_listWidget.setGeometry(QtCore.QRect(50, 220, 341, 451))
        self.lista_listWidget.setObjectName("lista_listWidget")

        self.ta_bort = QtWidgets.QPushButton(self.centralwidget)
        self.ta_bort.setGeometry(QtCore.QRect(170, 160, 91, 41))
        self.ta_bort.setObjectName("ta_bort")

        self.rensa_allt = QtWidgets.QPushButton(self.centralwidget)
        self.rensa_allt.setGeometry(QtCore.QRect(300, 160, 91, 41))
        self.rensa_allt.setObjectName("rensa_allt")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 435, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Day Planer"))
        self.lagg_till.setText(_translate("MainWindow", "Add"))
        self.ta_bort.setText(_translate("MainWindow", "Remove"))
        self.rensa_allt.setText(_translate("MainWindow", "Clear"))

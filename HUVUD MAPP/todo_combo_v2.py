from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCalendarWidget, QVBoxLayout
from PyQt5.QtCore import QDate
import json
import os
                            #Förklaring i stora drag:
# Import av moduler: Importerar nödvändiga bibliotek från PyQt5 för att skapa GUI 
# (grafiskt användargränssnitt), samt moduler för att hantera datum och filer (JSON och OS).

# Task-klassen: Skapar en klass för att representera en uppgift, som kan ha ett unikt ID, 
# kategori (beskrivning), och deadline. Just nu används den inte aktivt i koden.

# Ui_MainWindow-klassen: Huvudklassen som hanterar GUI-element som kalender, uppgiftslista, 
# inmatningsfält, och knappar.

# Setup av GUI-komponenter: Innehåller kod för att skapa och placera alla komponenter 
# (kalender, uppgiftslista, textfält, knappar) och applicera stil på dem.

# Kalenderwidget och uppgiftslista: Kalendern tillåter användare att välja datum. Uppgifterna 
# visas i en lista kopplad till det valda datumet.

# Inmatningsfält och knappar:  Användare kan skriva in nya uppgifter och ange en deadline, 
# som sedan kan läggas till eller tas bort från listan via "Add"- och "Remove"-knappar.

# Laddning av uppgifter:  Funktionen load_tasks_for_date laddar uppgifter från en fil (om den finns) 
# när ett nytt datum väljs i kalendern.

# Spara uppgifter: Funktionen save_tasks_for_date sparar aktuella uppgifter för det valda 
# datumet i en JSON-fil.

# Lägga till och ta bort uppgifter: Funktionen add_task lägger till en uppgift till listan, 
# och remove_task tar bort en vald uppgift från listan.

# Huvudprogrammet: Startar applikationen och visar huvudfönstret där användaren kan interagera 
# med gränssnittet.

class Task:
    def __init__(self, task_id, category, dead_line=None):
        self.task_id = task_id  # Unikt ID för varje uppgift
        self.category = category  # Uppgiftens namn eller kategori
        self.dead_line = dead_line  # Deadline för uppgiften, kan vara None om ingen deadline

    def __str__(self):
        return f"{self.task_id}. {self.category} (Time: {self.dead_line})"

# Huvudklassen för gränssnittet
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Ställer in huvudfönstret och dess egenskaper
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 791)
        MainWindow.setStyleSheet("background-color: #abdbe3;")  # Sätter bakgrundsfärgen

        # Central widget där alla andra widgets kommer att läggas
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Skapar en vertikal layout för att hålla alla widgets
        self.layout = QVBoxLayout(self.centralwidget)

        # Skapar en kalenderwidget där användaren kan välja datum
        self.calendar = QCalendarWidget(self.centralwidget)
        self.calendar.setGridVisible(True)  # Visar ett rutnät på kalendern
        self.layout.addWidget(self.calendar)  # Lägger till kalendern i layouten

        # Skapar en lista där uppgifter visas
        self.task_list = QtWidgets.QListWidget(self.centralwidget)
        self.task_list.setObjectName("task_list")
        self.task_list.setStyleSheet("""
            background-color: #ceedef;
            border-radius: 15px;
            border: 0px solid #000000;
        """)  # Sätter stilen för uppgiftslistan
        self.layout.addWidget(self.task_list)  # Lägger till uppgiftslistan i layouten

        # Skapar ett textfält där användaren kan skriva in nya uppgifter
        self.task_input = QtWidgets.QLineEdit(self.centralwidget)
        self.task_input.setStyleSheet("""
            background-color: white;
            border-radius: 15px;
            border: 0px solid #000000;
        """)  # Sätter stilen för textfältet
        self.layout.addWidget(self.task_input)  # Lägger till textfältet i layouten

        # Skapar ett textfält för att ange deadline
        self.deadline_input = QtWidgets.QLineEdit(self.centralwidget)
        self.deadline_input.setStyleSheet("""
            background-color: white;
            border-radius: 15px;
            border: 0px solid #000000;
        """)  # Sätter stilen för deadlinefältet
        self.layout.addWidget(self.deadline_input)  # Lägger till deadlinefältet i layouten

        # Skapar en knapp för att lägga till nya uppgifter
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setStyleSheet("""
            background-color: #14375c;
            border-radius: 15px;
            border: 0px solid #000000;
            color: white;
        """)  # Sätter stilen för knappen
        self.add_button.setText("Add")  # Sätter texten på knappen
        self.layout.addWidget(self.add_button)  # Lägger till knappen i layouten

        # Skapar en knapp för att ta bort uppgifter
        self.remove_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_button.setStyleSheet("""
            background-color: #14375c;
            border-radius: 15px;
            border: 0px solid #000000;
            color: white;
        """)  # Sätter stilen för knappen
        self.remove_button.setText("Remove")  # Sätter texten på knappen
        self.layout.addWidget(self.remove_button)  # Lägger till knappen i layouten

        # Sätter centralwidget som huvudfönstrets centrala komponent
        MainWindow.setCentralWidget(self.centralwidget)

        # Anropar funktionen som sätter text för knappar och fönster
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # En lista för att hålla alla uppgifter
        self.tasks = []

        # Kopplar knappar och kalender till sina respektive funktioner
        self.add_button.clicked.connect(self.add_task)  # Lägg till ny uppgift
        self.remove_button.clicked.connect(self.remove_task)  # Ta bort vald uppgift
        self.calendar.clicked.connect(self.load_tasks_for_date)  # Ladda uppgifter för valt datum

    # Funktion för att ladda uppgifter för valt datum
    def load_tasks_for_date(self, date):
        selected_date = date.toString("yyyy-MM-dd")  # Konverterar valt datum till en sträng
        tasks_file = f'tasks_{selected_date}.json'  # Filnamn för att spara/ladda uppgifter för det datumet

        # Om det finns en fil för valt datum, ladda uppgifterna
        if os.path.exists(tasks_file):
            with open(tasks_file, 'r') as file:
                self.tasks = json.load(file)  # Laddar uppgifterna från filen
                self.task_list.clear()  # Rensar den visuella uppgiftslistan
                self.task_list.addItems(self.tasks)  # Lägger till uppgifter i listan
        else:
            # Om ingen fil finns, börja med en tom lista
            self.tasks = []
            self.task_list.clear()

    # Funktion för att spara uppgifter för valt datum
    def save_tasks_for_date(self):
        selected_date = self.calendar.selectedDate().toString("yyyy-MM-dd")  # Hämta valt datum
        tasks_file = f'tasks_{selected_date}.json'  # Filnamn för att spara uppgifter

        # Spara uppgifterna till en JSON-fil
        with open(tasks_file, 'w') as file:
            json.dump(self.tasks, file)

    # Funktion för att lägga till en ny uppgift
    def add_task(self):
        task = self.task_input.text()  # Hämta uppgift från textfältet
        deadline = self.deadline_input.text()  # Hämta deadline från textfältet

        if task:  # Kontrollera att uppgiften inte är tom
            # Lägg till uppgiften i listan med deadline
            self.tasks.append(f"{task} - Time: {deadline}")
            self.task_list.addItem(f"{task} - Time: {deadline}")  # Visa uppgiften i listan
            self.task_input.clear()  # Rensa textfältet för uppgift
            self.deadline_input.clear()  # Rensa textfältet för deadline

            # Spara uppgifterna för valt datum
            self.save_tasks_for_date()

    # Funktion för att ta bort vald uppgift
    def remove_task(self):
        selected_items = self.task_list.selectedItems()  # Hämta de valda uppgifterna
        if not selected_items:  # Om inga uppgifter är valda, gör inget
            return
        for item in selected_items:  # För varje vald uppgift
            self.tasks.remove(item.text())  # Ta bort den från listan
            self.task_list.takeItem(self.task_list.row(item))  # Ta bort den från den visuella listan

        # Spara uppgifterna för valt datum
        self.save_tasks_for_date()

    # Funktion för att översätta texten för knappar och fönster
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Everything List"))  # Sätter fönstertiteln

# Huvudprogrammet som startar applikationen
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)  # Skapar en applikationsinstans
    MainWindow = QtWidgets.QMainWindow()  # Skapar huvudfönstret
    ui = Ui_MainWindow()  # Skapar en instans av användargränssnittet
    ui.setupUi(MainWindow)  # Sätter upp gränssnittet i huvudfönstret
    MainWindow.show()  # Visar huvudfönstret
    sys.exit(app.exec_())  # Startar applikationens huvudloop

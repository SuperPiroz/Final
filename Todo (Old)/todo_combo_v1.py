from PyQt5 import QtCore, QtGui, QtWidgets

#Förklaring:
#Task-klassen: Den representerar varje uppgift i listan, med ett unikt ID, en beskrivning (category) och en deadline.
#Ui_MainWindow: Denna klass hanterar själva gränssnittet och dess logik. Den innehåller alla widgets (som listan, inmatningsfälten, och knapparna) och metoder för att lägga till/ta bort uppgifter.
#Metoderna:
#setupUi: Skapar gränssnittet och placerar alla komponenter.
#retranslateUi: Används för att sätta texten på knappar och titlar.
#add_task: Lägger till en ny uppgift till listan.
#remove_task: Tar bort den valda uppgiften från listan.
#update_task_list: Uppdaterar den visuella listan med alla uppgifter.
#Huvudprogrammet: Skapar en instans av applikationen och visar huvudfönstret.


# En klass som representerar en uppgift (task) i ToDo-appen.
class Task:
    def __init__(self, task_id, category, dead_line=None):
        # Initialiserar en uppgift med ett unikt ID, en beskrivning (category) och en deadline.
        self.task_id = task_id  # Unikt ID för varje uppgift
        self.category = category  # Beskrivning av uppgiften
        self.dead_line = dead_line  # Deadline för uppgiften, kan vara None om ingen deadline anges

    # Denna metod gör att vi kan returnera en strängrepresentation av uppgiften
    def __str__(self):
        return f"{self.task_id}. {self.category} (Deadline: {self.dead_line})"

# Klass som ansvarar för att sätta upp och hantera huvudfönstret och alla gränssnittskomponenter
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Namnger huvudfönstret och sätter dess storlek
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 791)
        MainWindow.setStyleSheet("background-color: #abdbe3;") # färg för bakgrunden 

        # Skapar en central widget där alla andra widgets (knappar, textfält osv.) placeras
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Skapar en lista där vi kommer att visa alla uppgifter
        self.task_list = QtWidgets.QListWidget(self.centralwidget)
        self.task_list.setGeometry(QtCore.QRect(50, 50, 331, 491))  # Sätter position och storlek
        self.task_list.setObjectName("task_list")
        self.task_list.setStyleSheet("background-color: #ceedef;")  # ljusare blå för listan för uppgiftslistan
        
        # Skapar ett textfält där användaren kan skriva in nya uppgifter
        self.task_input = QtWidgets.QLineEdit(self.centralwidget)
        self.task_input.setGeometry(QtCore.QRect(50, 570, 171, 31))  # Position och storlek
        self.task_input.setObjectName("task_input")
        self.task_input.setStyleSheet("background-color: white;")  # Vit bakgrund för rutan 
        
        # Skapar ett textfält där användaren kan ange deadline för uppgiften
        self.deadline_input = QtWidgets.QLineEdit(self.centralwidget)
        self.deadline_input.setGeometry(QtCore.QRect(220, 570, 161, 31))  # Position och storlek
        self.deadline_input.setObjectName("deadline_input")
        self.deadline_input.setStyleSheet("background-color: white;")  # Vit bakgrund för rutan 

        # Skapar en knapp för att lägga till nya uppgifter
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(50, 620, 151, 41))  # Position och storlek
        self.add_button.setObjectName("add_button")
        self.add_button.setStyleSheet("background-color: white;")  # Vit bakgrund för rutan 
 
    
        # Skapar en knapp för att ta bort valda uppgifter från listan
        self.remove_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_button.setGeometry(QtCore.QRect(220, 620, 151, 41))  # Position och storlek
        self.remove_button.setObjectName("remove_button")
        self.remove_button.setStyleSheet("background-color: white;")  # Vit bakgrund för rutan 

        # Ställer in centralwidget som huvudfönstrets centrala komponent
        MainWindow.setCentralWidget(self.centralwidget)

        # Anropar metoden som översätter och sätter texten för knappar och fönster
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # En lista som kommer att hålla alla uppgifter (Task-objekt)
        self.tasks = []

        # Kopplar knapparna till sina respektive metoder
        self.add_button.clicked.connect(self.add_task)  # Lägg till ny uppgift
        self.remove_button.clicked.connect(self.remove_task)  # Ta bort vald uppgift

    def retranslateUi(self, MainWindow):
        # Sätter texten för fönstret och knapparna med hjälp av Qt's översättningssystem
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Everything List"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.remove_button.setText(_translate("MainWindow", "Remove"))

    # Metod för att lägga till en ny uppgift till listan
    def add_task(self):
        # Hämtar texten från inmatningsfälten
        task_text = self.task_input.text()  # Text för uppgiftsbeskrivningen
        deadline_text = self.deadline_input.text()  # Text för deadline

        # Kontrollera om uppgiftsbeskrivningen inte är tom
        if task_text:
            task_id = len(self.tasks) + 1  # Skapar ett nytt ID för uppgiften baserat på antalet befintliga uppgifter
            new_task = Task(task_id, task_text, deadline_text)  # Skapar en ny Task med input från användaren
            self.tasks.append(new_task)  # Lägger till den nya uppgiften i listan över uppgifter
            self.update_task_list()  # Uppdaterar listvyn så att nya uppgiften syns

            # Rensar textfälten efter att uppgiften har lagts till
            self.task_input.clear()
            self.deadline_input.clear()

    # Metod för att ta bort den valda uppgiften från listan
    def remove_task(self):
        selected_task = self.task_list.currentRow()  # Hämtar index för den markerade uppgiften
        if selected_task >= 0:  # Kontrollera att en uppgift är markerad
            self.tasks.pop(selected_task)  # Tar bort uppgiften från listan
            self.update_task_list()  # Uppdaterar listvyn

    # Uppdaterar listan med alla uppgifter som ska visas i gränssnittet
    def update_task_list(self):
        self.task_list.clear()  # Rensar den visuella listan först
        for task in self.tasks:  # Går igenom alla uppgifter
            self.task_list.addItem(str(task))  # Lägger till varje uppgift i listvyn

# Huvudprogrammet som startar appen
if __name__ == "__main__":
    import sys  # Importerar sys för att hantera systemrelaterade funktioner
    app = QtWidgets.QApplication(sys.argv)  # Skapar en applikationsinstans
    MainWindow = QtWidgets.QMainWindow()  # Skapar huvudfönstret
    ui = Ui_MainWindow()  # Skapar ett objekt av vårt gränssnitt
    ui.setupUi(MainWindow)  # Sätter upp gränssnittet i huvudfönstret
    MainWindow.show()  # Visar huvudfönstret
    sys.exit(app.exec_())  # Startar applikationens huvudloop (den kör så länge appen är igång)

import sys  # Importerar systemfunktioner för att hantera programflödet
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton  # Importerar PyQt5 komponenter för GUI
from PyQt5.QtCore import QProcess  # Importeras för att kunna starta externa program


# Huvudfönstret för appen
class MainApp(QWidget):
    def __init__(self):
        super().__init__()  # Initierar huvudklassen QWidget
        self.init_ui()  # Kallar på metod för att sätta upp gränssnittet
        self.process = None  # Variabel för att hantera de externa programmen

    # Metod för att skapa och visa layout och knappar
    def init_ui(self):
        self.setWindowTitle('Piroz Utilities')  # Titel på huvudfönstret

        layout = QVBoxLayout()  # Skapar en vertikal layout

        # Skapar knappar för varje program
        self.btn_raknare = QPushButton('Starta Räknare')  # Knappar för "räknare_combo_v2.py"
        self.btn_weather = QPushButton('Starta Väder App')  # Knappar för "wheater_v1.py"
        self.btn_todo = QPushButton('Starta To-Do App')  # Knappar för "todo_combo_v2.py"

        # Lägg till knappar i layouten
        layout.addWidget(self.btn_raknare)
        layout.addWidget(self.btn_weather)
        layout.addWidget(self.btn_todo)

        # Kopplar varje knapp till dess respektive funktion
        self.btn_raknare.clicked.connect(self.start_raknare)
        self.btn_weather.clicked.connect(self.start_weather)
        self.btn_todo.clicked.connect(self.start_todo)

        # Ställer in layouten för fönstret
        self.setLayout(layout)

    # Funktion för att starta "räknare_combo_v2.py"
    def start_raknare(self):
        if self.process is None:  # Om inget program redan körs
            self.process = QProcess(self)  # Skapar en ny process
            self.process.finished.connect(self.reset_process)  # När programmet stängs, reset
            # den fullständiga sökvägen om programmet inte finns i samma mapp
            self.process.start("python", ["/Users/mac/Desktop/Piroz_IT/AI_Pyton_gurnd/Projekt_ARB/HUVUD MAPP/räknare_combo_v2.py"])  #faktiska sökväg

    # Funktion för att starta "wheater_v1.py"
    def start_weather(self):
        if self.process is None:
            self.process = QProcess(self)
            self.process.finished.connect(self.reset_process)
            # den fullständiga sökvägen om programmet inte finns i samma mapp
            self.process.start("python", ["/Users/mac/Desktop/Piroz_IT/AI_Pyton_gurnd/Projekt_ARB/HUVUD MAPP/wheater_v1.py"])  #faktiska sökväg

    # Funktion för att starta "todo_combo_v2.py"
    def start_todo(self):
        if self.process is None:
            self.process = QProcess(self)
            self.process.finished.connect(self.reset_process)
            # den fullständiga sökvägen om programmet inte finns i samma mapp
            self.process.start("python", ["/Users/mac/Desktop/Piroz_IT/AI_Pyton_gurnd/Projekt_ARB/HUVUD MAPP/todo_combo_v2.py"])  #faktiska sökväg

    # När ett program stängs, sätt process till None för att kunna starta ett nytt
    def reset_process(self):
        self.process = None

# Skapar och kör huvudprogrammet
app = QApplication(sys.argv)
main_app = MainApp()
main_app.show()  # Visar huvudfönstret
sys.exit(app.exec_())  # Startar eventloopen och håller applikationen igång

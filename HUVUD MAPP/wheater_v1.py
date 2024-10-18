import sys  # Ger oss tillgång till system-specifika parametrar och funktioner
import requests  # Tar hand om API-förfrågningar och svar
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton  # Importerar PyQt5-komponenter för GUI
from PyQt5 import Qt  # Importerar andra QT-funktioner

                
                # Förklaring av koden i storadrag:
#Import: koden börjar med detta importera dom olika bibliotek som behövs. sys for system interaktion, 
# requests för att ta hand om API. PyQt5 komponenterna för att skapa en graphical user interface (GUI).

# klass defenition: WeatherApp klassen ärver från QWidget, som tillåterden att skapa ett fönster 
# med knappar, input fäält och display. klassen har metoder för att initiera och kontrolera appen.

# Andvändar gränsnitt setup: init:ui metoden samordnar layouten och elementen som text rutot , dispalay, och 
# och knappar ifönstret. den kopplar det knapparna gör med metoder som tar emot vädret när det klickas. 

# Hämtning av väder data: när andvändaren klickar på knappen, Show_weater metoden taremot en stads namn 
# från input boxen , hämtar väder och andvänder get_weahter funktionen, och visar resulltatet på skärmen. 
###

# En funktion för att hämta väderdata från OpenWeather API
def get_weather(city):
    api_key = "2bf9f8b496466d380866aabfccddcda3"  # Din API-nyckel för OpenWeatherMap
    base_url = "http://api.openweathermap.org/data/2.5/weather?"  # Bas-URL för API-anrop
    complete_url = f"{base_url}q={city}&appid={api_key}"  # Komplett URL med stadens namn och API-nyckel
    response = requests.get(complete_url)  # Skickar förfrågan till servern
    return response.json()  # Returnerar svar från servern i JSON-format

# En klassdefinition för väderappen som ärver från QWidget-klassen
class WeatherApp(QWidget):
    
    # En konstruktor-metod som automatiskt anropas när vi skapar en instans av WeatherApp-klassen
    def __init__(self):
        super().__init__()  # Kallar föräldraklassen (QWidget) och dess konstruktor för att initiera denna widget
        self.init_ui()  # Anropar en metod för att sätta upp användargränssnittet

    # Denna metod sätter upp den grafiska layouten och designen för appen
    def init_ui(self):
        self.setWindowTitle('Piroz Weather App')  # Sätter titeln på appfönstret
        
        # Skapar en vertikal layout och arrangerar de olika widgets i fönstret
        layout = QVBoxLayout()
        
        # En etikett som säger åt användaren att skriva in sitt stadsnamn
        self.city_label = QLabel('Enter city name:')
        
        # En textinput där användaren ska skriva in sitt stadsnamn
        self.city_input = QLineEdit()
        # text input layout 
        self.city_input.setStyleSheet("border-radius: 10px; border: 1px solid #ccc; padding: 5px;")

        # En knapp som användaren trycker på för att få väderinformationen
        self.get_weather_btn = QPushButton('Get Weather')
        
        
        # self.get_weather_btn.setStyleSheet är knapp layout
        
        #border-radius: 10px;: Detta gör hörnen rundade. Ju högre värde, desto mer rundade hörn får du.
        #border: 1px solid #ccc;: Detta ger en tunn, grå kant runt inmatningsrutan.
        #padding: 5px;: Detta ger lite utrymme inuti inmatningsrutan så att texten inte ligger direkt mot kanten.
        #background-color: #007BFF;: Detta ställer in bakgrundsfärgen för knappen.
        #color: white;: Detta sätter textfärgen för knappen till vit.
        #padding: 10px;: Detta ger lite utrymme inuti knappen så att texten ser bättre ut.
        self.get_weather_btn.setStyleSheet("border-radius: 10px; background-color: #007BFF; color: white; padding: 10px;")

        # En etikett som ska visa väderinformationen efter att den har hämtats
        self.weather_info = QLabel('')  # Tom från början, men senare ska den visa väderinformationen
        
        # Lägger till widgets till layouten en efter en
        layout.addWidget(self.city_label)  # Lägg till texten för stadsnamn
        layout.addWidget(self.city_input)  # Lägg till textinput
        layout.addWidget(self.get_weather_btn)  # Lägg till knappen
        layout.addWidget(self.weather_info)  # Lägg till etiketten för väderinformation
        
        # Sätter layouten till fönstret till den layout vi just skapade
        self.setLayout(layout)
        
        # Kopplar samman knappens klick-event med funktionen "show_weather"
        self.get_weather_btn.clicked.connect(self.show_weather)

    # Detta är metoden som kommer anropas när knappen trycks, den hämtar och visar väderdata
    def show_weather(self):
        # Hämtar stadsnamnet som användaren angav
        city = self.city_input.text()
        
        # Hämtar väderinformation genom att använda get_weather-funktionen
        weather_data = get_weather(city)
        
        try:
            # Extraherar temperaturen från datan och konverterar från Kelvin till Celsius
            temperature = weather_data['main']['temp'] - 273.15  # 'main' innehåller temperaturinformation i Kelvin
            
            # Extraherar väderbeskrivningen, t.ex. "klar himmel", "regn"
            description = weather_data['weather'][0]['description']
            
            # Visar väderinformationen i etiketten
            self.weather_info.setText(f"Temperature: {temperature:.2f} °C\nDescription: {description}")
        except KeyError:
            # Om staden inte hittas eller det blir ett fel, visar vi ett felmeddelande
            self.weather_info.setText("City not found.")  # Felmeddelande när staden inte hittas

# Startar PyQt5-programmet
app = QApplication(sys.argv)  # Skapar huvudapplikationsobjektet
weather_app = WeatherApp()  # Skapar en instans av appen
weather_app.show()  # Visar fönstret på skärmen
sys.exit(app.exec_())  # Ren exit när appen stängs



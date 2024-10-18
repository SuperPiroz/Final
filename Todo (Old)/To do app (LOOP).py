
import json
import os

# introducerar (punkter) som variabeln och lagrar den i json filen
try:
    with open('punkter.json') as f:
        punkter = json.load(f)
except FileNotFoundError:
    punkter = {}

# Variabl
ui_width = 50

while True:

    if os.name == 'posix':  # Rensa terminalen för Linux/macOS
        os.system('clear')
    else:  # Rensa terminalen för övriga OS
        os.system('cls')

    # Utseandet utgår från kompendium
    print('<<<TO DO LISTA>>>'.center(ui_width))
    print('*' * ui_width)

    # Skriv ut punkter (från jason filen punkter)
    for punkt in punkter:
        print('-', punkt)

    # Layout
    print('-' * ui_width)
    print('Titta | Titta på dina Todos')
    print('add   | Lägg till en Todo')
    print('tb    | Ta bort en Todo')
    print('exit  | Avsluta appen ')
    print('-' * ui_width)

    # user input
    val = input('menu > ').lower()

    # Valet titta
    if val == 'Titta':
        val_punkt = input('Title: >')
        try:
            print('-' * ui_width)
            print(f'{punkter[val_punkt]}')
            print('-' * ui_width)
            input('Tryck på enter för att fortsätta!')
        except KeyError:
            print(f'Fel. To do:n finns inte')
            input('Tryck på enter för att fortsätta!')

    # Valet add
    elif val == 'add':
        try:
            # Get user input
            print('-' * ui_width)
            val_title = input('Title >')
            val_descr = input('Descr >')

            # Try to add the note to the dict
            punkter[val_title] = val_descr

            # Layout
            print('-' * ui_width)
            print('INFO: Note added')
            print('-' * ui_width)
            input('Press any key to continue...')
        except:
            print('Unexpected error')

    # Valet att ta bort,  tb (remove)
    elif val == 'tb':
        try:
            val_tabort = input('Rubrik >')
            del punkter[val_tabort]

            # Layout
            print('-' * ui_width)
            print('Din to do har tagits bort!')
            print('-' * ui_width)
            input('Tryck på enter för att fortsätta!')
        except:
            print('Den Todo du angav finns inte!')
    # Valet att avsluta, exit
    elif val == 'exit':
        # Spara anteckningarna till JSON filen
        with open('punkter.json', 'w') as f:
            json.dump(punkter, f)
            print("Sparar allt i punkter.json")
            print("Tack för att du andvänder Piroz TO DO APP! ")
        break

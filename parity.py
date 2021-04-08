import sys
import os
from termcolor import colored, cprint
import time
from random import randint

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

title = None
summary = None
instructions = None
options = None
error = None
proposal_prompt = None
yay = None
aww = None
retry_prompt = None

language = None
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
answer = ""
result = False

class ErrorHandler:
    def __init__(self, state, message, waiting_time):
        cls()
        print(message)
        time.sleep(waiting_time)
        cls()
        if state == "language_select":
            language_select = LanguageSelect()
        elif state == "main_menu" or "parity_game":
            menu = MainMenu()
        else:
            cls()
            print("wtf did u do bru")
            time.sleep(100)

class LanguageSelect:
    def __init__(self):
        cls()
        global title
        global summary
        global instructions
        global options
        global error
        global proposal_prompt
        global yay
        global aww
        global retry_prompt
        language = input("Select your language and press Enter:\nEnglish = 1, Spanish = 2\n")
        if language == "1":
            title = "Welcome to Parity.py!\n"
            summary = "This is a command line game based on a common error control algorithm.\n"
            instructions = "The upmost row and the rightmost column give a clue to the error in the grid. When you think you've found it, input the error's coordinates (i.e. 4C) and press Enter to check!\n"
            options = "1. Easy   2. Normal   3. Hard   4. Exit\n"
            error = "The option you've inputted is not valid.\n"
            proposal_prompt = "\n\nResult: "
            yay = "Congratulations! You have succesfully cleared the game :)"
            aww = "Oh no! You failed to clear the game :("
            retry_prompt = "Try again? (Y/N): "
            menu = MainMenu()
        elif language == "2":
            title = "Bienvenido a Parity.py!\n"
            summary = "Este es un juego de línea de comandos basado en un algoritmo de control de errores común.\n"
            instructions = "La fila superior y la columna izquierda muestran pistas para encontrar el error en la cuadrícula. Cuando lo encuentres, ingresa las coordenadas del error (ej. 4C) y presiona Enter para verificar!\n"
            options = "1. Fácil   2. Normal   3. Dificil   4. Salir\n"
            error = "La opción que has ingresado no es válida.\n"
            proposal_prompt = "\n\nResultado: "
            yay = "Hurra! Ganaste el juego :)"
            aww = "Oh no! Perdiste el juego :("
            retry_prompt = "¿Quieres volver a intentar? (Y/N): "
            menu = MainMenu()
        else:
            language = ("Error")
            error = ErrorHandler("language_select", "The language you've inputted is not valid.\n", 3)

class MainMenu:
    def __init__(self):
        cls()
        print(title + summary + instructions + options)
        chosen_option = input()
        if chosen_option == "1":
            game = ParityGame(4, 4)
        elif chosen_option == "2":
            game = ParityGame(8, 8)
        elif chosen_option == "3":
            game = ParityGame(16, 16)
        elif chosen_option == "4":
            quit()
        else:
            chosen_option == "Error"
            error = ErrorHandler("main_menu", "Main menu input error.\n", 3)

class ParityGame:
    def __init__(self, field_width, field_height):
        self.field_width = field_width
        self.field_height = field_height
        answer = (abc[randint(0, field_height - 1)]) + str(randint(0, field_width - 1) + 1)
        proposal = ""

        def display_grid():
            # Create grid
            grid = []
            for i in range(0, field_height):
                row = []
                for i in range(0, field_width):
                    row.append(randint(0,1))
                grid.append(row)
            
            # Create error checking values
            hint_row = [0] * field_width
            hint_column = [0] * field_height
            column_count = 0
            row_count = 0
            for r in grid:
                for n in r:
                    hint_column[row_count] += n
                    hint_row[column_count] += n
                    column_count += 1
                hint_column[row_count] %= 2
                column_count = 0
                row_count += 1
            n = 0
            while n < field_width:
                hint_row[n] %= 2
                n += 1
            
            # Create parity bit value
            parity_bit = 0
            row_value = 0
            column_value = 0
            for n in hint_row:
                row_value += n
            row_value %= 2
            for n in hint_column:
                column_value += n
            column_value %= 2
            if row_value == column_value:
                if row_value == 0:
                    parity_bit = 0
                elif row_value == 1:
                    parity_bit = 1
            else:
                parity_bit = 0
                row_value = 0
                column_value = 0
                error = ErrorHandler("parity_game", "Mismatching parity values.\n", 3)

            # Display coordinate row
            print("    ", end = "")
            i = 0
            while i <= field_width:
                if i != 0:
                    print(i, end = " ")
                i += 1
            print("")
            
            # Display parity bit and error checking row
            print("  ", end = "")
            print(str(parity_bit), end = " ")
            i = 0
            for i in hint_row:
                print(i, end = " ")
            print("")

            # Display grid
            count = 0
            for r in grid:

                # Display coordinate and error checking columns
                print(str(abc[count]), end = " ")
                print(hint_column[count], end = " ")

                #Display grid columns
                for n in r:
                    print(str(n), end = " ")
                print()
                count += 1
        
        def check_result():
            print("Correct answer: " + answer)
            proposal = input(proposal_prompt)
            print("Correct answer: " + answer)
            print("Your response: " + proposal)
            time.sleep(1)
            if proposal == answer:
                return True
            else:
                return False
        
        cls()
        display_grid()
        if(check_result() == True):
            result = True
        else:
            result = False
        result_screen = ResultMenu(result)

class ResultMenu:
    def __init__(self, result):
        self.result = result
        if result == True:
            print(yay)
        else:
            print(aww)
        retry = input(retry_prompt)
        if retry == "Y" or "y":
            menu = MainMenu()
        else:
            menu = MainMenu()


language_select = LanguageSelect()

# TODO: Add color (examples below)

# text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
# print(text)
# print('Hello, World!', 'green', 'on_red')

# print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
# print_red_on_cyan('Hello, World!')
# print_red_on_cyan('Hello, Universe!')

# for i in range(10):
#     cprint(i, 'magenta', end=' ')

# cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)
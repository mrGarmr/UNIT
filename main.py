import random
import time

from rich.console import Console
from rich.table import Table

console = Console()


def commands():
    console.print("POSSIBLE COMMANDS:\n", style='bold blue')
    console.print("1. ", style="")
    console.print("If you want to exit - type exit!", style='blue')
    time.sleep(1)
    console.print("2. ", style="")
    console.print("If you want to read rules - type help!", style='blue')
    time.sleep(1)


def exits():
    clear()
    console.print("\nHave a nice day! Good bye!!!\n", style="bold underline green")
    return False


def error_handler(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except:
            result = input_error()
            return result

    return inner


@error_handler
def main():
    process = True
    while process:
        console.print('\n                    Would you like to play a GAME?                    ',
                      style='bold underline blue on white')

        console.print(100 * '_', style='bold red')
        console.print('\n   "game" for starting new game\n   "help" for rules.\n   "exit" to exit\n', style='bold blue')
        user_input = input('>>>> ')
        console.print(100 * '_', style='bold red')
        user_input = user_input.lower()
        result = handler(user_input)
        if result:
            print(result)
        elif result is None:
            pass
        elif not result:
            process = False
        else:
            break


def get_word():
    with open("words.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).rstrip()


def handler(user_input):
    if user_input in ANSWEARS.keys():
        return ANSWEARS[user_input]()

    else:
        return input_error()


def clear():
    print("\033c", end="")


def helps():
    clear()
    console.print("Help & Shortcuts:\n\n")
    console.print("1. ", style="green")
    console.print("Read Rules\n")
    console.print("2. ", style="green")
    console.print("Commands\n")
    console.print("3. ", style="green")
    console.print("All\n\n")
    h_user = input(">>>> ")
    if h_user == "1":
        rules()
    if h_user == "2":
        commands()
        clear()
    if h_user == "3":
        rules()
        commands()


def loose(secret_word):
    clear()
    console.print("                   YOU LOOSE!!!                   ", style='bold underline red on white')
    console.print(f"           THE SECRET WORD WAS: {secret_word}    ", style='bold underline red on white')
    time.sleep(1)

    with open("hang.txt", "r") as f:
        lines = f.read()
        print(lines)


def rules():
    clear()
    console.print("The RULES of Hangman:\n", style='bold blue')
    console.print("1. ", style="")
    console.print("The computer ask a word - you have to guess it!", style='blue')
    time.sleep(1)
    console.print("2. ", style="green")
    console.print(
        "The word is obscured with question marks, but as you guess the correct letters, it will reveal itself.",
        style='blue')
    time.sleep(1)
    console.print("3. ", style="green")
    console.print("Each turn, you can either guess a letter or enter a command.", style='blue')
    time.sleep(1)
    console.print("4. ", style="green")
    console.print("If your guessed letter is in the word, the letter will reveal itself and appear ", style='blue')
    console.print("green ", style="bold green")
    console.print("in the turn log.", style='blue')
    time.sleep(1)
    console.print("5. ", style="green")
    console.print("If your guessed letter is not in the word, you will loose one try of 6 and the letter will appear",
                  style='blue')
    console.print("red ", style="bold red")
    console.print("in the turn log.", style='blue')
    time.sleep(1)
    console.print("6. ", style="green")
    console.print("To win, you must guess the word correctly with fewer than 6 mistakes.\n", style='blue')
    time.sleep(1)
    console.print("Good luck! And LET THE GAME START!!!!", style="bold underline green on red")


def game():
    secret_word = get_word()
    console.print('I made up a word. Guess a word', style='bold underline cyan on white')
    lifes = 6
    letters = ''
    secret_list = list(len(secret_word) * '*')

    while lifes > 0:
        if '*' in secret_list:
            table(lifes, letters, secret_list)
            console.print('Guess a letter or word: ', style='bold underline cyan on white')
            guess_word = input('>>>> ')
            if guess_word == 'exit':
                exits()
                break

            if guess_word in secret_word:
                console.print(f'Letter "{guess_word}" is in this word! Good choice.',
                              style='bold underline green on white')
                letters += ' ' + guess_word
                count = secret_word.count(guess_word)
                index = 0

                for i in range(count):
                    index = secret_word.find(guess_word, index)
                    secret_list[index] = guess_word

            else:
                console.print(f'Letter "{guess_word}" not in this word! You have lost 1 life',
                              style='bold underline red on white')
                lifes -= 1
                letters += ' ' + guess_word
        else:
            win(secret_word)
            break
        
    if lifes == 0 and ('*' in secret_list):
        loose(secret_word)


def greeting():
    console.print(101 * '*', style='bold red')
    time.sleep(0.05)
    console.print(
        r"*      __    __        ___      .__   __.   _______ .___  ___.      ___      .__   __.              *",
        style='bold red')
    time.sleep(0.05)
    console.print(
        r"*     |  |  |  |     //   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  |              *",
        style='bold red')
    time.sleep(0.05)
    console.print(
        r"*     |  |__|  |    //  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |              *",
        style='bold red')
    time.sleep(0.05)
    console.print(
        r"*     |   __   |   //  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |              *",
        style='bold red')
    time.sleep(0.05)
    console.print(
        r"*     |  |  |  |  //  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |              *",
        style='bold red')
    time.sleep(0.05)
    console.print(
        r"*     |__|  |__| //__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__|              *",
        style='bold red')
    time.sleep(0.05)
    console.print(101 * '*', style='bold red')


def input_error():
    return 'Wrong input! Type exact command you want to do,"exit" to exit or "help" for list of commands.'


def table(lifes, letters, secret_list):
    view = '|'.join(secret_list)
    table = Table(title="GAME INFORMATION", style="cyan")

    table.add_column("LIFES", style="RED", no_wrap=True)
    table.add_column("Word", justify="center", style="magenta")
    table.add_column("USED LETTERS", justify="right", style="green")

    table.add_row(f':beating_heart: {lifes}')
    table.add_row(" ", view, letters)
    console.print(table, justify="center")

    return "ok"


def win(secret_word):
    clear()
    console.print("                   YOU WIN!!!                   ", style='bold underline green on white')
    console.print(f"           THE SECRET WORD WAS: {secret_word}    ", style='bold underline green on white')
    time.sleep(1)

    with open("win.txt", "r") as f:
        lines = f.read()
        print(lines)


ANSWEARS = {'play': game, 'game': game, 'help': helps, 'rules': helps, 'clear': clear, 'exit': exits, 'commands': commands}

if __name__ == '__main__':
    greeting()
    main()

HELP = ['&', '?', 'hlp', 'what', 'why', 'where', 'how', 'elp', 'hep', 'hel', 'healp', 'halp', 'hhelp', 'heelp', 'hellp',
        'helpp', 'рфдз', 'рдз', 'руз', 'руд', 'помощь']

import pyfiglet
import katscraper
import katparser


def printTitleScreen():
    result = pyfiglet.figlet_format("Kattis Analyzer")
    print(result)

if __name__ == "__main__":
    printTitleScreen()
    print("What do you want to do? (enter help for help)")
    while True:
        cliInput = input()
        cliInput = cliInput.lower()

        # Mega grim løsning.. men switch findes ikke i python så blev lige sådan her sofar
        # Der findes pænere løsning vi kan lave. Fx noget ala https://data-flair.training/blogs/python-switch-case/
        if cliInput == 'help':
            print("The following commands are allowed:")
            print("help - shows this option")
            print("scrape - Scrapes Kattis for info")
            print("parse - start parsing data from kattis")
            print("title - Reprints the title screen")
            print("exit - Exits the program")
        elif cliInput == 'title':
            printTitleScreen()
        elif cliInput == "scrape":
            katscraper.scrape()
        elif cliInput == "parse":
            katparser.parse()
        elif cliInput == 'exit':
            break
        else:
            print("Command unknown, type 'help' for a list of commands")

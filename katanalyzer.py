import pyfiglet
import os
import katscraper
import katparser


def print_title_screen():
    result = pyfiglet.figlet_format("Kattis Analyzer")
    print(result)


if __name__ == "__main__":
    print_title_screen()

    print("What do you want to do? (enter help for help)")
    while True:
        cli_input = input()
        cli_input = cli_input.lower()

        # Mega grim løsning.. men switch findes ikke i python så blev lige sådan her sofar
        # Der findes pænere løsning vi kan lave. Fx noget ala https://data-flair.training/blogs/python-switch-case/
        if cli_input == 'help':
            print("The following commands are supported:")
            print("help - shows this option")
            print("scrape - scrapes Kattis for info, requires email/password in credentials.txt or cookie in sessionid.txt (see README.md)")
            print("analyze - starts analyzing data from Kattis")
            print("title - reprints the title screen")
            print("exit - exits the program")
        elif cli_input == "title":
            print_title_screen()
        elif cli_input == "scrape":
            if not os.path.exists("sessionid.txt"):
                credentials_file = "credentials.txt"
                if not os.path.exists(credentials_file):
                    open(credentials_file, "w+")
                    print("Scraping requires credentials.txt with your Kattis email:password")
                    continue
                with open("credentials.txt", "r") as f:
                    username, password = f.readline().split(":")
                    katscraper.scrape(username, password)
            else:
                katscraper.scrape(None, None)
        elif cli_input == "analyze":
            katparser.parse(None)
        elif cli_input == 'exit':
            break
        else:
            print("Command unknown, type 'help' for a list of commands")

from colorama import init
from ui.cli import CLI

def main():
    init()  # Initialize colorama
    cli = CLI()
    cli.start()

if __name__ == "__main__":
    main()
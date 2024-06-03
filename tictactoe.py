import os.path
from network import Network
from game import TicTacToe

network = Network()


def start_game():
    print("\nAre you a host or a client?")

    while True:
        player = input("\nEnter host/client: ")
        if player == "host":
            network.host()
            you = "X"
            opponent = "O"
            break
        elif player == "client":
            network.connect_to_host()
            you = "O"
            opponent = "X"
            break
        else:
            print("Wrong input, try again")

    game = TicTacToe()
    game.you = you
    game.opponent = opponent
    game.handle_connection(network.client)


def configure():
    print("\nLet's setup network data for the game")
    print("Data can be autoloaded on start from default.txt")
    print("!DISCLAIMER! Network data user for both hosting and connecting ")

    while True:
        print("\nYou can input network data, save it to file or load it from file and return to main menu")
        setup = input("Enter input/save/load/back: ")
        if setup == "input":
            network.input_network_data()
        elif setup == "save":
            filename = input("Enter filename: ")
            network.save_data(filename)
        elif setup == "load":
            filename = input("Enter filename: ")
            network.load_data(filename)
        elif setup == "back":
            break
        else:
            print("Wrong input, try again")


if __name__ == "__main__":
    print("\nWelcome to online Tic-Tac-Toe!")

    if os.path.isfile("default.txt"):
        network.load_data("default")
    else:
        print("You need to enter the network data before you can play with other people")
        configure()

    while True:
        print("\nYou can play a game, configure network data or quit")
        choice = input("Enter play/configure/quit: ")
        if choice == "play":
            start_game()
        elif choice == "configure":
            configure()
        elif choice == "quit":
            print("Thank you for playing!")
            break
        else:
            print("Wrong input, try again")

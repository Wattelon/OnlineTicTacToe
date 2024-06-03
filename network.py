import socket


class Network:
    def __init__(self):
        self.address = None
        self.port = None
        self.client = None

    def input_network_data(self):
        print("Specify host address and port")
        print("You can leave empty address if you wish it to be set to this host automatically")

        while True:
            self.address = input("Input host in 0.0.0.0 format: ")
            if len(self.address.split('.')) == 4 and all([i.isdigit() for i in self.address.split('.')]):
                break
            elif len(self.address) == 0:
                self.address = socket.gethostbyname(socket.gethostname())
                break
            else:
                print("Wrong input, try again")

        while True:
            self.port = input("Input port in 0000 format: ")
            if len(self.port) == 4 and self.port.isdigit():
                self.port = int(self.port)
                break
            else:
                print("Wrong input, try again")

        print("Network data accepted")

    def host(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.address, self.port))
        server.listen(1)

        print("Waiting for client...")
        self.client, address = server.accept()
        print(f"Client {address} connected!")

    def connect_to_host(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("Connecting to host...")
        self.client.connect((self.address, self.port))
        print("Connected!")

    def save_data(self, filename):
        with open(filename + ".txt", "w") as file:
            file.write(f"{self.address}\n{self.port}")
        print(f"Data saved in {filename}.txt!")

    def load_data(self, filename):
        try:
            with open(filename + ".txt", "r") as file:
                self.address = file.readline().strip()
                self.port = int(file.readline())
            print(f"Data loaded from {filename}.txt!")
            print(f"Current address is {self.address}, current port is {self.port}")
        except FileNotFoundError as error:
            print(error)

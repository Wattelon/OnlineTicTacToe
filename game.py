class TicTacToe:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = "X"
        self.you = "X"
        self.opponent = "O"
        self.winner = None
        self.game_over = False
        self.counter = 0

    def handle_connection(self, client):
        while not self.game_over:
            if self.turn == self.you:
                move = input("Enter a move in row,column format: ")
                if self.check_valid_move(move):
                    client.send(move.encode('utf-8'))
                    self.apply_move(move.split(','), self.you)
                    self.turn = self.opponent
                else:
                    print("Invalid move!")
            else:
                print("Waiting for opponent's turn...")
                data = client.recv(1024)
                if not data:
                    break
                else:
                    self.apply_move(data.decode('utf-8').split(','), self.opponent)
                    self.turn = self.you
        client.close()

    def apply_move(self, move, player):
        if self.game_over:
            return
        self.counter += 1
        self.board[int(move[0])][int(move[1])] = player
        self.print_board()
        if self.check_if_won():
            if self.winner == self.you:
                print("You win!")
            elif self.winner == self.opponent:
                print("You lose!")
        else:
            if self.counter == 9:
                print("It is a tie!")

    def check_valid_move(self, move):
        if len(move) == 3:
            if move[0].isdigit() and move[1] == "," and move[2].isdigit():
                row, column = map(int, move.split(","))
                if row < 3 and column < 3:
                    return self.board[row][column] == " "
        return False

    def check_if_won(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                self.winner = self.board[row][0]
                self.game_over = True
                return True
        for column in range(3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] != " ":
                self.winner = self.board[0][column]
                self.game_over = True
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            self.winner = self.board[1][1]
            self.game_over = True
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            self.winner = self.board[1][1]
            self.game_over = True
            return True
        return False

    def print_board(self):
        for row in range(3):
            print(" | ".join(self.board[row]))
            if row != 2:
                print("---------")
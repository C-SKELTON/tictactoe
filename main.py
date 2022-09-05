class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def choose_spot(self, row, col, player):
        self.board[row][col] = player

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def change_player(self, player):
        if player == 'X':
            return '0'
        return 'X'

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def did_player_win(self, player):
        win = None
        n = len(self.board)
        #check rows 123, 456, 789
        for i in range(n):
            win = True
            for j in range(n):
                #print(self.board[i][j])
                if self.board[i][j] != player:
                    win = False
            if win:
                return win

        #check columns 147, 258, 369
        for i in range(n):
            win = True
            for j in range(n):
                #print(self.board[j][i])
                if self.board[j][i] != player:
                    win = False
            if win:
                return win

        #check diagonals 159, 357
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                #print(self.board[i][i])
                win = False
        if win:
            return win



    def start(self):
        self.create_board()

        player = 'X'
        while True:
            print(f"Player {player} turn")
            self.show_board()

            #taking user input
            user_choice = input("pick row and column: ")
            row = int(user_choice[0])
            col = int(user_choice[1])

            #logging_letter
            self.choose_spot(row, col, player)
            print(self.board)

            #did player win
            if self.did_player_win(player):
                print(f"Player {player} wins the game!")
                break

            #check for draw
            if self.is_board_filled():
                print("Match Draw!")
                break

            #change player
            player = self.change_player(player)


        # showing the final view of board
        print()
        self.show_board()


tic_tac_toe = TicTacToe()
tic_tac_toe.start()
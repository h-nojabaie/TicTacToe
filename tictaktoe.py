
import random


class TicTacToe:

    def __init__(self,dim,playerNum):
        self.dim=dim
        self.playerNum=playerNum
        self.board = []

    def create_board(self):
        for i in range(self.dim):
            row = []
            for j in range(self.dim):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return str (random.randint(1, self.playerNum))

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)
        # checking rows
        for i in range(n):
            win=False
            counter=0
            for j in range(n):
                if self.board[i][j] != player:
                    counter=0
                else:
                    counter=counter+1
                    if counter==3:
                        win=True;

                        break;

            if win:
                return win
            


        # checking columns
        for i in range(n):
            win=False
            counter=0
            for j in range(n):
                if self.board[j][i] != player:
                    counter=0
                else:
                    counter=counter+1
                    if counter==3:
                        win=True;
                        break;

            if win:
                return win

        # checking diagonals
        win=False
        counter=0
        for i in range(n):
            if self.board[i][i] != player:
                counter=0
            else:
                counter=counter+1
                if counter==3:
                    win=True;
                    break;
        if win:
            return win

        win=False
        counter=0
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                counter=0
            else:
                counter=counter+1
                if counter==3:
                    win=True;
                    break;
        if win:
            return win
        
        return False


    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        player=int(player)
        player=player+1
        if player>self.playerNum:
            player=1
        return str(player)

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = self.get_random_first_player()
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
print("inert your dim game:")
dim=int(input())
print("inert your players number:")
playerNum=int(input())

tic_tac_toe = TicTacToe(dim,playerNum)
tic_tac_toe.start()

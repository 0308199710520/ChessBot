import attr


@attr.s
class Piece:
    name = attr.ib(type=str)
    colour = attr.ib(type=str)


@attr.s
class Square:
    id = attr.ib(type=int)
    piece = attr.ib(type=str)
    square_colour = attr.ib(type=str, default="White")

    def colour_setter(self):
        """
        Sets the colours of the squares on the board, currently its only setup for string reps, but in the future will
        set the references directly for the graphics generator.
        :return:
        """
        if self.square_colour is None:
            # This line swaps the colours every new line
            if (self.id + self.id // 8) % 2 == 1:
                self.square_colour = "black_square"
            else:
                self.square_colour = "white_square"
        else:
            pass


@attr.s
class Board:
    # Board holds all the positional data turn to turn, the groundwork that the game is built on
    board = attr.ib(attr.Factory(list))

    def setup(self, start: str = ""):

        """
        Generates 64 squares for the board, starting top left (White Square) and moving to the bottom right id's 0-63
        """
        for i in range(0, 64):
            self.board.append(Square(i, None, None))
            self.board[i].colour_setter()
        if start is None:
            # FEN representation of a starting setup in chess
            self.FEN_translator_in("RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr")
        else:
            self.FEN_translator_in(start)

    def FEN_translator_in(self, FEN_string: str):
        id_pointer = 0
        print(FEN_string)
        pieces_dict = {
            "P": "pawn_white",
            "N": "knight_white",
            "B": "bishop_white",
            "R": "rook_white",
            "Q": "queen_white",
            "K": "king_white",
            "p": "pawn_black",
            "n": "knight_black",
            "b": "bishop_black",
            "r": "rook_black",
            "q": "queen_black",
            "k": "king_black",
        }

        for character in range(len(FEN_string)):
            if FEN_string[character] == "/":
                continue
            if FEN_string[character].isdigit():
                for i in range(int(FEN_string[character])):
                    self.board[id_pointer].piece = None
                    id_pointer += 1
            else:
                print("this has been called")

                self.board[id_pointer].piece = pieces_dict[FEN_string[character]]
                id_pointer += 1
                # do something FDGSLJNBDSAKHJGBKHJRFBDFKJHGNBsdl;ikfjmcvlkj

    # DEPRECATED!!! Literally just for Debugging atm I HATE HOW THIS IS AND IT NEEDS A COMPLETE REDESIGN TO SCALE IT
    def board_printer(self):

        id_pointer = 0

        while id_pointer is not (len(self.board)):
            print(f"|{' ' * ((21 * 8) - 1)}|")
            print_string = ""
            for _ in range(8):
                if self.board[id_pointer].piece is not None:
                    print_string += f"|{self.board[id_pointer].piece:^20}"

                else:
                    print_string += f"|{'Square':^20}"

                id_pointer += 1

            print_string += "|"
            print(print_string)
            print(f"|{' ' * ((21 * 8) - 1)}|")
            print("-" * 21 * 8)


@attr.s
class GameLogic:
    board = attr.ib(attr.Factory(list))

    def move_list(self):
        pass

    def _pawn(self, colour):
        if colour == "white":
            return (+8, +16, +7, + 9)
        else:
            return (-8, -16, -7, -9)

    def _castle(self, colour):
        pass



a = Board()

a.setup(start="rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R")

print(a.board)

a.board_printer()

print(a.board)

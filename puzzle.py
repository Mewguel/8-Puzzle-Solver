# import section
from tile import Tile

MAX_NUM_TILES = 9

# class declaration
class Puzzle:
    
    # add more attributes
    def __init__(self):
        self.board = []
        self.no_of_moves = 0

    # trigger tile swap
    # swap clicked tile to the empty tile
    # empty tile is a special type of tile unclickable
    def swap_tiles(self):
        self.board
        # swap swap_tiles

    
    def create_board(self):
        image_num = 1
        for i in range(MAX_NUM_TILES//3):
            for j in range(MAX_NUM_TILES//3):
                # assign empty tile Tile 0
                if image_num == MAX_NUM_TILES:
                    image_num = 0
                self.board.append(Tile(i,j,image_num))
                image_num += 1
        self.show_board()


    def show_board(self):
        #replace by tkinter show Tile Components
        for i in range(MAX_NUM_TILES):
            if i % 3 == 0:
                print()
            print(f"{self.board[i].img}", end=" ")
        print()


if __name__ == "__main__":
    board = Puzzle()
    board.create_board()
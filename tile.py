# import section


# class declaration
class Tile:
    
    # add image on the tile
    def __init__(self, x_pos, y_pos, image):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.img = image
        self.is_movable = False


    def change_pos(self, new_x, new_y):
        if self.is_movable:
            self.x_pos = new_x
            self.y_pos = new_y





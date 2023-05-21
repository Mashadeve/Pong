from settings import *


class Slider:
    def __init__(self, x, y):
        self.slider_size = SLIDER_SIZE
        self.slider_pos_x = x
        self.slider_pos_y = y

    def move(self, direction):
        self.slider_pos_y += direction * 5
        

from settings import *
import random

class Ball:

    def __init__(self):
        self.vx = -1 * 250
        self.vy = 0
        self.x = WIDTH/2
        self.y = HEIGHT/2

    def move(self):
        self.x += 1/FPS * self.vx
        self.y += 1/FPS * self.vy
    
    def collisions(self, slider_left_pos, slider_right_pos):
        left_x , left_y = slider_left_pos
        right_x , right_y = slider_right_pos
        print(left_x+SLIDER_WIDTH)
        print(left_y+SLIDER_HEIGHT)
        if (self.x <= left_x+SLIDER_WIDTH) and (left_y <= self.y < left_y+SLIDER_HEIGHT):
            self.vx *= -1.5




    


    

    
    
from settings import *
import random 
class Ball:

    def __init__(self):
        self.vx = random.randrange(-1, 2, 2) * 250
        self.vy = 0
        self.x = WIDTH/2
        self.y = HEIGHT/2

    def move(self):
        self.x += 1/FPS * self.vx

    


    

    
    
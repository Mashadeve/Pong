from settings import *
import random 
class Ball:

    def __init__(self):
        self.velocity = vx, vy =  (random.randrange(-1, 2, 2), 1) 
        self.coords = x, y = (WIDTH/2, HEIGHT/2)

    def move(self):
        self.coords += FPS * self.velocity
        

    

    
    
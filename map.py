import pygame as pg
from settings import *
from slider import *

class Map:

    def __init__(self, screen):
        self.screen = screen
        self.slider_left = Slider(LEFT)
        self.slider_right = Slider(RIGHT)

    def drawBall(self):
        pg.draw.circle(self.screen, WHITE, CENTER, 5)

    def drawSliders(self):
        pg.draw.rect(self.screen, WHITE, pg.Rect(self.slider_left.slider_pos,self.slider_left.slider_size))
        pg.draw.rect(self.screen, WHITE, pg.Rect(self.slider_right.slider_pos, self.slider_right.slider_size))
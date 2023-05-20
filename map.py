import pygame as pg
from settings import *
from slider import *
from ball import Ball

class Map:

    def __init__(self, screen):
        self.screen = screen
        self.slider_left = Slider(LEFT)
        self.slider_right = Slider(RIGHT)
        self.ball = Ball()
       

    def drawBall(self):
        pg.draw.circle(self.screen, WHITE, (self.ball.x, self.ball.y), 5)
        self.ball.move()

    def drawSliders(self):
        pg.draw.rect(self.screen, WHITE, pg.Rect(self.slider_left.slider_pos,self.slider_left.slider_size))
        pg.draw.rect(self.screen, WHITE, pg.Rect(self.slider_right.slider_pos, self.slider_right.slider_size))
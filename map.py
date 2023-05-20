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
       

    def draw_ball(self):
        pg.draw.circle(self.screen, WHITE, (self.ball.x, self.ball.y), BALL_RADIUS)
        self.ball.move()
        self.ball.collisions(self.slider_left.slider_pos, self.slider_right.slider_size)

    def draw_sliders(self):
        pg.draw.rect(self.screen, WHITE, pg.Rect(self.slider_left.slider_pos,self.slider_left.slider_size))
        pg.draw.rect(self.screen, WHITE, pg.Rect(self.slider_right.slider_pos, self.slider_right.slider_size))
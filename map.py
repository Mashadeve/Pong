import pygame as pg
from settings import *
from slider import *
from ball import Ball
import random

class Map:

    

    def __init__(self, screen, slider_left, slider_right):
        self.screen = screen
        self.slider_left = slider_left
        self.slider_right = slider_right
        self.left_score = 0
        self.right_score = 0
        self.ball = Ball()
       

    def draw_ball(self, slider_left, slider_right):
        l_x, l_y = slider_left.slider_pos_x, slider_left.slider_pos_y
        r_x, r_y = slider_right.slider_pos_x, self.slider_right.slider_pos_y
        pg.draw.circle(self.screen, WHITE, (self.ball.x, self.ball.y), BALL_RADIUS)
        self.ball.move()
        self.ball.collisions((l_x, l_y), (r_x, r_y))

        if self.ball.check_position() == "LEFT":
            self.right_score += 1
            self.ball.x = WIDTH/2
            self.ball.y = HEIGHT/2
            self.ball.vx = [1, -1][int(round(random.random()))] * 250
            self.ball.vy = [1, -1][int(round(random.random()))] * 100
            
        if self.ball.check_position() == "RIGHT":
            self.left_score += 1
            self.ball.x = WIDTH/2
            self.ball.y = HEIGHT/2
            self.ball.vx = [1, -1][int(round(random.random()))] * 250
            self.ball.vy = [1, -1][int(round(random.random()))] * 100

    def draw_sliders(self, slider_left, slider_right):
        l_x, l_y = slider_left.slider_pos_x, slider_left.slider_pos_y
        r_x, r_y = slider_right.slider_pos_x, slider_right.slider_pos_y
        pg.draw.rect(self.screen, WHITE, pg.Rect((l_x, l_y), slider_left.slider_size))
        pg.draw.rect(self.screen, WHITE, pg.Rect((r_x, r_y), slider_right.slider_size))

    def draw_all(self, slider_left, slider_right):
        self.draw_ball(slider_left, slider_right)
        self.draw_sliders(slider_left, slider_right)
        self.draw_score()

    def draw_score(self):
        font = pg.font.Font('freesansbold.ttf', 32)
        text = font.render(f'{self.left_score} - {self.right_score}', True, WHITE, BLACK)
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, 50)
        self.screen.blit(text, textRect)



    

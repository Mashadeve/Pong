import pygame as pg
from settings import *

class Map:

    def __init__(self, screen):
        self.screen = screen

    def drawBall(self):
        pg.draw.circle(self.screen, (255, 255, 255), (WIDTH/2, HEIGHT/2), 5)
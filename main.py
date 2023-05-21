import pygame as pg
import sys
from settings import *
from map import Map
from slider import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.slider_left = Slider(LEFT_X, LEFT_Y)
        self.slider_right = Slider(RIGHT_X, RIGHT_Y)
        self.map = Map(self.screen, self.slider_left, self.slider_right)

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f"{self.clock.get_fps() :.1f}")

    def draw(self):
        self.screen.fill("black")
        self.map.draw_all(self.slider_left, self.slider_right)

    def check_events(self):
        key_input = pg.key.get_pressed()
        pg.key.set_repeat()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
   
        key_input = pg.key.get_pressed()
        if key_input[pg.K_UP]:
            self.slider_left.move(-1)
        if key_input[pg.K_DOWN]:
            self.slider_left.move(1)
        if key_input[pg.K_w]:
            self.slider_right.move(-1)
        if key_input[pg.K_s]:
            self.slider_right.move(1)


    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()

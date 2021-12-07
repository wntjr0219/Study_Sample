from pico2d import *

class World:
    def __init__(self):
        self.image = load_image('mario_world_1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1600, 284)
  

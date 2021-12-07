import random

from pico2d import *

import game_framework
import game_world

import server
import collision

class Brick:
    #클래스 변수
    BOY_X0, BOY_Y0 = -50, 60

    def __init__(self, center=300, y=100):
        self.image = load_image('brick180x40.png')
        self.left_wall, self.right_wall = center - 100, center + 100
        self.x, self.y = center, y
        self.speed = random.randint(100,250) * random.choice([-1,1])

    def update(self):
        self.x += game_framework.frame_time * self.speed
        if self.x >= self.right_wall:
            self.speed = random.randint(100,250) * random.choice([-1,1])
            self.x = self.right_wall
        if self.x <= self.left_wall:
            self.speed = random.randint(100,250) * random.choice([-1,1])
            self.x = self.left_wall

        # 발판과 소년이 충돌하는지 체크
        # if collision.collide(self, server.boy):
        #     server.boy.set_parent(self) #boy를 brick의 자식으로 만듬
           
    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x-90, self.y-20, self.x+90, self.y+20

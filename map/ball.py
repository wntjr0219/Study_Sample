from pico2d import *
import game_world
import game_framework
class Ball:
    image = None

    def __init__(self, x = 400, y = 300, dir = 1):
        PIXEL_PER_METER = (10.0 / 0.3)
        BALL_SPEED_KMPH = 108.4
        BALL_SPEED_MPM = (BALL_SPEED_KMPH * 1000.0 / 60.0)
        BALL_SPEED_MPS = (BALL_SPEED_MPM / 60.0)
        BALL_SPEED_PPS = (BALL_SPEED_MPS* PIXEL_PER_METER)

        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y , self.dir =  x, y, dir
        self.velocity = self.dir * BALL_SPEED_PPS

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity * game_framework.frame_time

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

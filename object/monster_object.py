from pico2d import *
import random
import game_framework
import game_world
import server

#8(?)주차 적군 기본 오브젝트

#아직 샘플만 구현됨

PIXEL_PER_METER = (10.0 / 0.3) # 0.3미터당 10픽셀
RUN_SPEED_KMPH = random.randint(100,250)
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 // 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM // 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Monster:
    image = None

    def __init__(self): 
        self.x, self.y = random.randint(100, 700), random.randint(70, 80)
        self.frame = 0
        self.speed = random.randint(10,25)
        self.dir = random.choice([-1,1])
        self.timer = random.randint(30, 60)

        if Monster.image == None:
            self.image = load_image('gomba_motion.png')

    def update(self): 
        global RUN_SPEED_PPS
        self.frame = (self.frame +  FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7
        
    
        # 움직임 대충 구현
        self.timer -= 1
        velocity = self.speed * self.dir
        self.x += velocity * game_framework.frame_time
        if self.timer == 0:
            self.speed = random.randint(100,250)
            self.dir = self.dir * -1
            velocity = self.speed * self.dir
            self.x += velocity * game_framework.frame_time
        
        self.x = clamp(25, self.x, 1600 - 25)
        
    def get_bb(self):
        return self.x-30, self.y-30, self.x+30, self.y+30

    # def update(self):
    #     self.x += game_framework.frame_time * self.speed
    #     if self.x >= self.right_wall:
    #         self.speed = random.randint(100,250) * random.choice([-1,1])
    #         self.x = self.right_wall
    #     if self.x <= self.left_wall:
    #         self.speed = random.randint(100,250) * random.choice([-1,1])
    #         self.x = self.left_wall
        
    def draw(self): 
        if self.dir == 1:
            self.image.clip_draw(int(self.frame) * 65, 0 * 75, 65, 75, self.x, self.y)
        else:
            self.image.clip_draw(int(self.frame) * 65, 1 * 75, 65, 75, self.x, self.y)
        draw_rectangle(*self.get_bb())




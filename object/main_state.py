import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball
from brick import Brick
from monster_object import Monster
import server
name = "MainState"






def enter():
    server.boy = Boy()
    game_world.add_object(server.boy, 1)

    server.grass = Grass()
    game_world.add_object(server.grass, 0)

    # server.bricks = [Brick(300+300*i, 100+50*i) for i in range(5)]
    server.bricks = [Brick(300+300*i, 100+50*i) for i in range(5)] # test
    game_world.add_objects(server.bricks, 1)

    server.monsters = [Monster() for i in range(1)] # test
    game_world.add_objects(server.monsters, 1)



def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            server.boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # 발판에서 체크
    # for brick in bricks:
    #         if collide(boy, brick):
    #             boy.x  = brick.x
    #             boy.y  = brick.y + 70
    #             boy.x = clamp(brick.x - 90, boy.x, brick.x + 90)





def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







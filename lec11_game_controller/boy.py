from pico2d import *

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP = range(4)
# fill here

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP
}



# Boy States
class Idlestate:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_DOWN:
            boy.velocity += 1
        boy.timer = 1000

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1

    def draw(boy):
        if boy.dir ==1:
            pass


next_state_table = {
# fill here
}







class Boy:

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        # fill here
        self.frame = 0
        self.timer = 0
        # self.event_que = []
        # self.cur_state = IdleState
        # self.cur_state.enter(self, None)
        pass


    def change_state(self,  state):
        # fill here
        pass


    def add_event(self, event):
        self.event_que.insert(0, event)
     

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que > 0):
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
             

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

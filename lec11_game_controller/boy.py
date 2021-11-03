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

# fill here

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
        # fill here
        pass


    def update(self):
        # fill here
        pass


    def draw(self):
        # fill here
        pass


    def handle_event(self, event):
        # fill here
        pass

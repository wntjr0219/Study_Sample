# class Star:
# # 생성자 함수가 꼭 필요하지는 않다 -> 객체를 한번만 찍어내는 용도
#     type = 'Star'
#     x = 100 # class 변수

#     def change():
#         x = 200 # local 변수
#         print('x is ', x)

# print('x is ', Star.x)
# Star.change()
# print('x is ', Star.x)

# star = Star() # 클래스 변수는 객체변수처럼 사용가능
# print('x is ', star.x)
# # star.change() # 에러  # star.change() -> Star.change(star)

# # 파이썬의 모든 변수는 포인터임
# # self는 자기자신을 참조하는 매개변수

class Player:
    type = 'Player'
    
    def __init__(self):
        self.x = 100

    def where(self):
        print(self.x)


player = Player()
player.where()

print(player.type)
# Player.where()
Player.where(player)
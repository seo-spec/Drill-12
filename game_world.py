#world = [] #1차원 리스트

world = [[],[]] #월드의 2차원 리스트
#0번, 1번 레이어를 가지는 2차원 리스트

# 게임 월드 객체 추가, layer를 지정해야 한다.
def add_object(o,depth=0): #기본 depth=0으로, 즉 0번 레이어 추가
    world[depth].append(o)

#게임 월드에서 객체를 제거
def remove_object(o):
    for layer in world:
        if(o in layer):
            layer.remove(o)
            return # 더 이상 찾을 필요가 없으므로 return으로 종료, 최적화
        
#game logic
def update():
    # 업데이트 도중 공이 제거되어도 다음 객체를 건너뛰지 않는다.
    for layer in world:
        for o in layer:
            o.update()

#game rendering
def render():
    for layer in world:
        for o in layer:
            o.draw()

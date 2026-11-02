from pico2d import load_image

class Forest:
    def __init__(self):
        self.image = load_image('grass.png')
    
    def draw(self):
        self.image.clip_draw(0,25,800,62,400, 20)
    
    def update(self):
        pass
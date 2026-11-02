from pico2d import load_image

class Forest:
    def __init__(self):
        self.image = load_image('grass.png')
    
    def draw(self):
        self.image.clip_draw(0,31,800,62,400, 30)
    
    def update(self):
        pass
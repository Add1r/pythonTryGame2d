import pyxel

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Hero:
    def __init__(self, img_id):
        self.pos = Position(0,0)
        self.img_hero = img_id
        self.img_size_x = 10
        self.img_size_y = 10
        self.color_tr = 0
    
    def update(self, x, y):
        self.pos.x = x
        self.pos.y = y

class App:
    def __init__(self):
        self.IMG_IDO = 1
        self.WINDOW_H = 120
        self.WINDOW_W = 200

        pyxel.init(self.WINDOW_W, self.WINDOW_H, caption='Game-Version-1')
        pyxel.image(0).load(0,0, 'img/fon.png')
        pyxel.image(1).load(0,0, 'img/hero.png')

        self.hero = Hero(self.IMG_IDO)
        self.hero.pos.x = 0
        self.hero.pos.y = 0

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.hero.pos.y - 1 > 0 and pyxel.btn(pyxel.KEY_W):
            self.hero.update(self.hero.pos.x, self.hero.pos.y - 2)
        if self.hero.pos.x - 1 > 0 and pyxel.btn(pyxel.KEY_A):
            self.hero.update(self.hero.pos.x - 2, self.hero.pos.y)
        if self.hero.pos.y + 23 < self.WINDOW_H and pyxel.btn(pyxel.KEY_S):
            self.hero.update(self.hero.pos.x, self.hero.pos.y + 2)
        if self.hero.pos.x + 21 < self.WINDOW_W and pyxel.btn(pyxel.KEY_D):
            self.hero.update(self.hero.pos.x + 2, self.hero.pos.y)

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.hero.pos.x, self.hero.pos.y, self.hero.img_hero, 0 ,0, self.hero.img_size_x, self.hero.img_size_y, self.hero.color_tr)

App()
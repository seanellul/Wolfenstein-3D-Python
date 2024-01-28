import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'RaycastingGame/resources/sound/'
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
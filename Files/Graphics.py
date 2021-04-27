import pygame
import os, sys
from pygame.locals import *

if not pygame.font():
    print("Warning, fonts disabled")

if not pygame.mixer:
    print("Warning, mixer disabled")


def load_image(name, colourkey=None):
    fullname = os.path.join("Data/Images", name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print("Cannot load image: ", name)
        raise SystemExit(message)
    image = image.convert()
    if colourkey is not None:
        if colourkey is -1:
            colourkey = image.get_at((0, 0))
        image.set_colourkey(colourkey, RLEACCEL)
    return image, image.get_rect()


def load_sounds(name):
    class NoneSound:
        def play(self):
            pass

    if not pygame.mixer:
        return NoneSound()

    fullname = os.path.join("Data/Sounds", name)

    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print("Cannot load sound:", fullname)
        raise SystemExit(message)
    return sound


class Piece(pygame.sprite.Sprite):

    def __init__(self, Piece_ID):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(Piece_ID, -1)

    def move(self):
        pass

    def _take(self):
        pass


pygame.display.init()
pygame.init()

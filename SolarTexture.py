__author__ = 'Bernhard Schwertberger und Isabella DallOglio '

from OpenGL.GL import *
import pyglet.image
from pyglet.gl import *

class solarTexture:

    suntexture = None
    merkurtexture = None
    venustexture = None
    erdetexture = None
    marstexture = None
    jupitertexture = None
    saturntexture = None
    uranustexture = None
    neptuntexture = None

    def loadTexture(self, filename):
        '''
        Ein Bild wird ueber pyglet geladen um fuer eine Textur verwendet zu werden.
        :param filename:
        :return:
        '''
        image = pyglet.image.load(filename)
        return image

    def setupTexture(self):
        '''
        Texturen werden aktiviert und fuer jede Variable wird eine Textur geladen.
        :return:
        '''
        glEnable(GL_TEXTURE_2D)

        self.suntexture = self.loadTexture("data/sonne.png")
        self.merkurtexture = self.loadTexture("data/merkur.jpg")
        self.venustexture = self.loadTexture("data/venus.png")
        self.erdetexture = self.loadTexture("data/erde.jpg")
        self.marstexture = self.loadTexture("data/mars.png")
        self.jupitertexture = self.loadTexture("data/jupiter.png")
        self.saturntexture = self.loadTexture("data/saturn.png")
        self.uranustexture = self.loadTexture("data/uranus.png")
        self.neptuntexture = self.loadTexture("data/neptun.png")


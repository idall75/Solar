__author__ = 'Berni'

import unittest
from OpenGL.GL import *
from Solarwindow import solarwindow
from SolarTexture import solarTexture
import pyglet.image
from pyglet.gl import *

class TextureTest(unittest.TestCase):
    def test_texture(self):
        window = solarwindow()
        window.setupsplash(100,100)
        window.setupgl()

        tex = solarTexture()

        testtex = tex.loadTexture("sonne.jpg")

        if glIsEnabled(GL_TEXTURE_2D) == GL_TRUE:
            self.assertEqual(1, 1)
            self.assertEqual(testtex, tex.suntexture)

if __name__ == '__main__':
    unittest.main()

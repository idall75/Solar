__author__ = 'Berni'

import unittest
from OpenGL.GLU import *

from Solarwindow import solarwindow
from SolarPlanet import solarplanet
from SolarTexture import solarTexture

class PlanetTest(unittest.TestCase):
    def test_something(self):
        window = solarwindow()
        window.setupsplash(100,100)
        window.setupgl()

        sphere = gluNewQuadric()

        tex = solarTexture()
        tex.setupTexture()

        plan = solarplanet()

        plan.planet(1, sphere, tex.suntexture)

        plan.sun(0.5, sphere, tex.suntexture)

        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

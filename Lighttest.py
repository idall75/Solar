__author__ = 'Berni'

import unittest
from OpenGL.GL import *
from SolarLight import solarLight
from Solarwindow import solarwindow


class LightTest(unittest.TestCase):
    def test_something(self):
        window = solarwindow()
        window.setupsplash(100,100)
        window.setupgl()

        light = solarLight()
        light.setupLight()

        if glIsEnabled(GL_LIGHTING) == GL_TRUE and glIsEnabled(GL_NORMALIZE) == GL_TRUE and glIsEnabled(GL_LIGHT0) == GL_TRUE:
            self.assertEqual(1,1)
        else:
            self.assertEqual(1,2)



if __name__ == '__main__':
    unittest.main()

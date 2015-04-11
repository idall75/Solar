__author__ = 'Berni'

import unittest
import pygame
from pygame.locals import *
from Solarwindow import solarwindow


class WindowTest(unittest.TestCase):
    def test_setupsplash(self):
        window = solarwindow()
        window.setupsplash(100,100)

        screen = pygame.display.set_mode((100,100))

        self.assertEqual(window.screen, screen)

    def test_setupgl(self):
        window = solarwindow()
        window.setupsplash(100,100)
        window.setupgl()

        screen = pygame.display.set_mode((100,100), DOUBLEBUF | OPENGL)

        self.assertEqual(window.screen,screen)

    def test_resetup(self):
        window = solarwindow()
        window.setupsplash(100,100)
        window.setupgl()
        window.resetup()

        screen = pygame.display.set_mode((100,100))

        self.assertEqual(window.screen,screen)

if __name__ == '__main__':
    unittest.main()

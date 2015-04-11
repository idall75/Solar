__author__ = 'Bernhard Schwertberger, Isabella Dall Oglio'

import sys
from Solarwindow import solarwindow
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from SolarTexture import solarTexture
from SolarPlanet import solarplanet
from SolarLight import solarLight


class Solarmain:

    def main():
        '''
        Die Main - Methode handelt die Steuerung des gesamten Programms und führt den
        Code der verschiedenen Klassen zusammen.
        :return:
        '''

        #Variablen die zur steuerung des Programms benötigt werden.
        modestatus = 1
        lighting = False
        speed = 1
        yrot = speed
        distanceset = 0
        textureon = True
        lightingon = True
        cammode = 1

        #Initialisierung von Pygame
        pygame.init()

        #Objekt erstellung der anderen Klassen.
        window = solarwindow()
        window.setupsplash(1280,720)

        textures = solarTexture()

        planets = solarplanet()

        light = solarLight()

        #Endlosschleife die zur Darstellung des Programms benoetigt wird (erneutes Zeichnen)
        while True:
            if modestatus == 1:
                #blit zeichnet eine Grafik auf die Flaeche des Fensters
                window.screen.blit(window.splashscreen, (0, 0))

                #For Schleife die eingaben ueberwacht.
                for event in pygame.event.get():
                    #Wenn das x im Fenster gedrueckt wird wird die Applikation beendet
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    #Ueberprueft ob ein 'Key' auf der Tastatur betaetigt wurde.
                    elif event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            modestatus = 2

                #pygame.wait laesst die Applikation fuer einen bestimmten Zeitraum angegeben in ms warten.
                pygame.time.wait(1)

            elif modestatus == 2:
                window.setupgl()

                #Erstellung der Quadrics fuer die erstellung der Planeten
                sphere = gluNewQuadric()
                gluQuadricNormals(sphere, GL_FLAT)
                gluQuadricTexture(sphere, GL_TRUE)

                #Setup der Texturen
                textures.setupTexture()
                #Setup des Lichts
                light.setupLight()

                modestatus = 3

            elif modestatus == 3:
                #Position der Kamera
                if distanceset == 0 and cammode == 1:
                    gluLookAt(0,0,7,0,0,0,0,1,0)
                    distanceset = 1
                elif distanceset == 0 and cammode == 2:
                    gluLookAt(0,5,7,0,0,0,0,1,0)
                    distanceset = 1

                #Clearen der Buffer
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

                #PushMatrix und PopMatrix um die Darstellung der Translationen und Rotationen
                #richtig gewaehrleistet wird.
                #Zeichnen der Sonne
                glPushMatrix()
                glRotatef(yrot, 0, 1, 0)
                if lightingon:
                    glDisable(GL_LIGHTING)
                glRotatef(90, 1, 0, 0)
                planets.planet(1, sphere, textures.suntexture)
                glRotatef(-90, 1, 0, 0)
                if lightingon:
                    glEnable(GL_LIGHTING)
                glPopMatrix()

                #Zeichnen des Merkurs
                glPushMatrix()
                glRotatef(4.5 * yrot, 0, 1, 0.3)
                glTranslatef(2, 0, 0)
                glRotatef(yrot*3, 0, 1, 0)
                glRotatef(90, 1, 0, 0)
                planets.planet(0.035, sphere, textures.merkurtexture)
                glRotatef(-90, 1, 0, 0)
                glPopMatrix()

                #Zeichnen der Venus
                glPushMatrix()
                glRotatef(1.6 * yrot, 0, 1, 0.3)
                glTranslatef(3, 0, 0)
                glRotatef(yrot*3, 0, 1, 0)
                glRotatef(90, 1, 0, 0)
                planets.planet(0.086, sphere, textures.venustexture)
                glRotatef(-90, 1, 0, 0)
                glPopMatrix()

                #Zeichnen der Erde
                glPushMatrix()
                glRotatef(yrot, 0, 1, 0.3)
                glTranslatef(4, 0, 0)
                glRotatef(yrot*3, 0, 1, 0)
                glRotatef(90, 1, 0, 0)
                planets.planet(0.091, sphere, textures.erdetexture)
                glRotatef(-90, 1, 0, 0)
                #Zeichnen des Mondes
                glRotatef(-yrot*5, 0, 1, 0)
                glRotatef(12 * yrot, 0, 1, 0)
                glTranslatef(0.2, 0, 0.1)
                glRotatef(yrot*3, 0, 1, 0)
                glRotatef(90, 1, 0, 0)
                planets.moon(0.025, sphere, textures.merkurtexture)
                glRotatef(-90, 1, 0, 0)
                glPopMatrix()

                #Zeichnen des Mars
                glPushMatrix()
                glRotatef(yrot / 2, 0, 1, 0.3)
                glTranslatef(5, 0, 0)
                glRotatef(yrot*3, 0, 1, 0)
                glRotatef(90, 1, 0, 0)
                planets.planet(0.049, sphere, textures.marstexture)
                glRotatef(-90, 1, 0, 0)
                glPopMatrix()

                #Zeichnen des Jupiters
                glPushMatrix()
                glRotatef(yrot / 12, 0, 1, 0.3)
                glTranslatef(7, 0, 0)
                glRotatef(yrot*3, 0, 1, 0)
                glRotatef(90, 1, 0, 0)
                planets.planet(0.102, sphere, textures.jupitertexture)
                glRotatef(-90, 1, 0, 0)
                glPopMatrix()

                #Zeichnen des Saturns
                glPushMatrix()
                glRotatef(yrot / 30, 0, 1, 0.3)
                glTranslatef(9, 0, 0)
                glRotatef(yrot*3, 0, 1, 0)
                glRotatef(90, 1, 0, 0)
                planets.planet(0.086, sphere, textures.saturntexture)
                glRotatef(-90, 1, 0, 0)
                glPopMatrix()

                #Zeichnen des Uranus
                glPushMatrix()
                glRotatef(yrot / 84, 0, 1, 0.3)
                glTranslatef(11, 0, 0)
                glRotatef(yrot*3, 0, 1, 0)
                glRotatef(90, 1, 0, 0)
                planets.planet(0.037, sphere, textures.uranustexture)
                glRotatef(-90, 1, 0, 0)
                glPopMatrix()

                #Zeichnen des Neptuns
                glPushMatrix()
                glRotatef(yrot / 164, 0, 1, 0.3)
                glTranslatef(12, 0, 0)
                glRotatef(yrot*3, 0, 1, 0)
                glRotatef(90, 1, 0, 0)
                planets.planet(0.035, sphere, textures.neptuntexture)
                glRotatef(-90, 1, 0, 0)
                glPopMatrix()

                #Variable die die Rotation gewaehrleistet
                yrot += speed

                #Wait von 10 ms um die Darstellung der Grafik zu optimieren.
                pygame.time.wait(10)

                #Ueberwachung auf Eingabe
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    #Ueberwachung auf Key Eingaben auf der Tastatur
                    elif event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            modestatus = 4
                            distanceset = 0

                        #Steuerung der Geschwindigkeit ueber die rechte und linke Pfeiltaste.
                        if event.key == pygame.K_RIGHT and speed < 5:
                            speed += 0.5
                        if event.key == pygame.K_LEFT and speed > 0:
                            speed -= 0.5

                        #Steuerung der Kameraposition ueber die obere und untere Pfeiltaste.
                        if event.key == pygame.K_UP and cammode == 1:
                            cammode = 2
                            glLoadIdentity()

                            gluPerspective(window.fov, (window.size[0] / window.size[1]), 0.1, 100)
                            distanceset = 0

                        if event.key == pygame.K_DOWN and cammode == 2:
                            cammode = 1
                            glLoadIdentity()

                            gluPerspective(window.fov, (window.size[0] / window.size[1]), 0.1, 100)
                            distanceset = 0

                    #Ueberwachung auf Mauseingaben
                    elif event.type == MOUSEBUTTONDOWN:

                        #Steuerung des Zooms ueber das Mausrad.
                        if event.button == 4 and window.fov > 50:
                            window.fov -= 5
                            glLoadIdentity()

                            gluPerspective(window.fov, (window.size[0] / window.size[1]), 1.0, 100)
                            distanceset = 0

                        elif event.button == 5 and window.fov < 150:
                            window.fov += 5
                            glLoadIdentity()
                            gluPerspective(window.fov, (window.size[0] / window.size[1]), 1.0, 100)
                            distanceset = 0

                        #Steuerung der Texturen ueber klick der linken Maustaste
                        elif event.button == 1 and textureon == True:
                            glDisable(GL_TEXTURE_2D)
                            textureon = False
                        elif event.button == 1 and textureon == False:
                            glEnable(GL_TEXTURE_2D)
                            textureon = True

                        #Steuerung des Lichts ueber klick der rechten Maustaste
                        elif event.button == 3 and lightingon == True:
                            glDisable(GL_LIGHTING)
                            lightingon = False
                        elif event.button == 3 and lightingon == False:
                            glEnable(GL_LIGHTING)
                            lightingon = True

                glFlush()

            #Reset auf den Splashscreen
            elif modestatus == 4:
                window.resetup()
                modestatus = 1


            #Flip um das Bild zu aktualisieren.
            pygame.display.flip()


#Ausfuehrung der main Funktion
Solarmain.main()
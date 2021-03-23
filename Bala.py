from OpenGL.GL import *
from glew_wish import *
import glfw

from math import *

class Bala:
    desfase = 90
    velocidad = 1.0    
    posicionX = 0.0
    posicionY = 0.0
    angulo = 0.0

    def dibujar(self):
        glPushMatrix()
        glTranslate(self.posicionX, self.posicionY, 0.0)
        glRotate(self.angulo, 0.0, 0.0, 1.0)
        glBegin(GL_QUADS)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f(-0.01, 0.01, 0.0)
        glVertex3f(0.01, 0.01, 0.0)
        glVertex3f(0.01, -0.01, 0.0)
        glVertex3f(-0.01, -0.01, 0.0)
        glEnd()
        glPopMatrix()

    def actualizar(self, tiempo_delta):
        #global obstaculo
        self.posicionY = self.posicionY + \
            (sin((self.angulo + self.desfase) * 3.14159 / 180) * self.velocidad * tiempo_delta)
        self.posicionX = self.posicionX + \
            (cos((self.angulo + self.desfase) * 3.14159 / 180) * self.velocidad * tiempo_delta)
        # checar colision con obstaculo si sigue "vivo"
        #if obstaculo.Vivo and self.posicionX + 0.01 > obstaculo.PosicionX - 0.15 and self.posicionX - 0.01 < obstaculo.PosicionX + 0.15 and self.posicionY + 0.01 > obstaculo.PosicionY - 0.15 and self.posicionY - 0.01 < obstaculo.PosicionY + 0.15:
            #   obstaculo.Vivo = False
            #  carrito.disparando = False
from glew_wish import *
import glfw
from OpenGL.GL import *
class Obstaculo:
    PosicionX = 0.0
    PosicionY = 0.0
    Vivo = True

    def __init__(self, x, y):
        self.PosicionX = x
        self.PosicionY = y

    def dibuja(self):

        if self.Vivo:
            glPushMatrix()
            glTranslate(self.PosicionX, self.PosicionY, 0.0)
            glBegin(GL_QUADS)
            glColor3f(0.0, 0.0, 1.0)
            glVertex(-0.15, 0.15, 0.0)
            glVertex(0.15, 0.15, 0.0)
            glVertex(0.15, -0.15, 0.0)
            glVertex(-0.15, -0.15, 0.0)
            glEnd()
            glPopMatrix()
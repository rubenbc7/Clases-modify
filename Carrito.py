from glew_wish import *
import glfw
from math import *
from OpenGL.GL import *
from Bala import *

bala = Bala()
class Carrito:
    posicionX = 0
    posicionY = -0.8
    angulo = 0
    desfase = 90
    velocidad = 1
    velocidad_angular = 180
    disparando = False
    colisionando = False


    def disparar(self):
        global bala
        self.disparando = True
        bala.posicionX = self.posicionX
        bala.posicionY = self.posicionY
        bala.angulo = self.angulo
    
    def actualizar(self, window, tiempo_delta):
        global bala
        estadoIzquierda = glfw.get_key(window, glfw.KEY_LEFT)
        estadoDerecha = glfw.get_key(window, glfw.KEY_RIGHT)
        estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)
        estadoArriba = glfw.get_key(window, glfw.KEY_UP)

        if estadoIzquierda == glfw.PRESS:
            self.angulo = self.angulo + (self.velocidad_angular * tiempo_delta)
            if self.angulo > 360:
                self.angulo = 0
        if estadoDerecha == glfw.PRESS:
            self.angulo = self.angulo - (self.velocidad_angular * tiempo_delta)
            if self.angulo < 0:
                self.angulo = 360
        if estadoArriba == glfw.PRESS:
            self.posicionY = self.posicionY + \
                (sin((self.angulo + self.desfase) * 3.14159 / 180) * self.velocidad * tiempo_delta)
            self.posicionX = self.posicionX + \
                (cos((self.angulo + self.desfase) * 3.14159 / 180) * self.velocidad * tiempo_delta)
       
        if self.disparando:
            if bala.posicionX >= 1:
                self.disparando = False
            elif bala.posicionX <= -1:
                self.disparando = False
            elif bala.posicionY >= 1:
                self.disparando = False
            elif bala.posicionY <= -1:
                self.disparando = False

        if self.disparando:
            bala.actualizar(tiempo_delta)        

    def dibujarCarrito(self):
        global bala
        glPushMatrix()
        glTranslate(self.posicionX, self.posicionY, 0.0)
        glRotate(self.angulo, 0.0, 0.0, 1.0)
        glBegin(GL_TRIANGLES)
        if self.colisionando == True:
            glColor3f(1.0, 1.0, 1.0)
        else:
            glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 0.05, 0.0)
        glVertex3f(-0.05, -0.05, 0.0)
        glVertex3f(0.05, -0.05, 0.0)
        glEnd()
        glPopMatrix()

        if self.disparando:
            bala.dibujar()
        
    def checar_colision(self, obstaculo):
        # Si extremaDerechaCarrito > extremaIzquierdaObstaculo
        # Y extremaIzquierdaCarrito < extremaDerechaObstaculo
        # Y extremoSuperiorCarrito > extremoInferiorObstaculo
        # Y extremoInferiorCarrito < extremoSuperiorObstaculo
        if self.posicionX + 0.05 > obstaculo.PosicionX - 0.15 and self.posicionX - 0.05 < obstaculo.PosicionX + 0.15 and self.posicionY + 0.05 > obstaculo.PosicionY - 0.15 and self.posicionY - 0.05 < obstaculo.PosicionY + 0.15:
            self.colisionando = True
        else:
            self.colisionando = False

        if self.disparando and obstaculo.Vivo and bala.posicionX + 0.01 > obstaculo.PosicionX - 0.15 and bala.posicionX - 0.01 < obstaculo.PosicionX + 0.15 and bala.posicionY + 0.01 > obstaculo.PosicionY - 0.15 and bala.posicionY - 0.01 < obstaculo.PosicionY + 0.15:
            obstaculo.Vivo = False
            self.disparando = False
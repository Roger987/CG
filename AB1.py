from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from collections import namedtuple 

WINDOW_WIDTH = 850
WINDOW_HEIGHT = 850

UNIT_PIXEL = 1

class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

eye = Vector(0, 20, 30)
center = Vector(0, 0, 0)
up = Vector(0, 1, 0)
xBola = 0
yBola = -3.4
zBola = 0

score1 = 0
score2 = 0

colors ={
    "green": [1/255, 188/255, 1/255],
    "brown": [118/255, 74/255, 43/255],
    "white": [255, 255, 255]
}

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0) 
    
    update_camera()
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, WINDOW_WIDTH/WINDOW_HEIGHT, 0.1, 100.)
    glMatrixMode(GL_MODELVIEW)

def update_camera():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(eye.x   , eye.y   , eye.z,
              center.x, center.y, center.z,
              up.x    , up.y    , up.z)

    # print(f"_________________")
    # print(f"eye: ({eye.x}, {eye.y}, {eye.z})")
    # print(f"center: ({center.x}, {center.y}, {center.z})")
    # print(f"up: ({up.x}, {up.y}, {up.z})")

def draw_barra_vertical(x, y, z):
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glColor3fv(colors["white"])
    glScalef(0.5,3,0.5)
    glTranslatef(x, y, z)
    glutSolidCube(UNIT_PIXEL)
    glPopMatrix()  

def draw_barra_horizontal(x, y, z):
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glColor3fv(colors["white"])
    glScalef(0.5,0.5,5.5)
    glTranslatef(x, y, z)
    glutSolidCube(UNIT_PIXEL)
    glPopMatrix()  

def draw_bola():
    global xBola
    global yBola
    global zBola
    glPushMatrix()
    glColor3fv(colors["white"])
    glTranslatef(xBola, yBola, zBola) # movimenta a bola
    glutSolidSphere(0.5, 100, 100)
    glPopMatrix()

def draw_campo():
    glColor3fv(colors["green"])
    glPushMatrix()
    glTranslatef(0, -4, 0)
    glScalef(20, 0.01, -12)
    glutSolidCube(UNIT_PIXEL)
    glPopMatrix()

def bresenhamH(x1,z1,x2,z2):
    dz = z2-z1
    dx = x2-x1
    d = 2*dx - dz
    E = 2*dx
    NE = 2*(dx-dz)
    x = x1
    z = z1
    glBegin(GL_POINTS)
    glColor3f(255,255,255)
    glVertex3f(x,-3.99,z)
    glEnd()
    while z<z2:
        if d <= 0:
            d = d + E
            z = z + 0.01
        else:
            d = d + NE
            x = x + 0.01
            z = z + 0.01
        glBegin(GL_POINTS)
        glColor3f(255,255,255)
        glVertex3f(x,-3.99,z)
        glEnd()

def bresenhamV(x1,z1,x2,z2):
    dz = z2-z1
    dx = x2-x1
    d = 2*dz - dx
    E = 2*dz
    NE = 2*(dz-dx)
    x = x1
    z = z1
    glBegin(GL_POINTS)
    glColor3f(255,255,255)
    glVertex3f(x,-3.99,z)
    glEnd()
    while x<x2:
        # print(z)
        if d <= 0:
            d = d + E
            x = x + 0.01
        else:
            d = d + NE
            x = x + 0.01
            z = z + 0.01
        glBegin(GL_POINTS)
        glColor3f(255,255,255)
        glVertex3f(x,-3.99,z)
        glEnd()

def drawCircle(xc,x,zc,z):
    glBegin(GL_POINTS)
    glColor3f(255,255,255)
    glVertex3f(xc+x,-3.99,zc+z)
    glVertex3f(xc+x,-3.99,zc-z)
    glVertex3f(xc-x,-3.99,zc+z)
    glVertex3f(xc-x,-3.99,zc-z)
    glVertex3f(xc+z,-3.99,zc+x)
    glVertex3f(xc+z,-3.99,zc-x)
    glVertex3f(xc-z,-3.99,zc+x)
    glVertex3f(xc-z,-3.99,zc-x)
    glEnd()

def circle(xc,zc,r):
    x = 0
    z = r
    d = 5/4 - r
    drawCircle(xc,x,zc,z)
    while z>x:
        if d < 0:
            d = d + 2*x + 0.003
            x = x + 0.001
        else:
            d = d + 2*(x-z) +0.005
            x = x + 0.001
            z = z - 0.001
        drawCircle(xc,x,zc,z)

def display():
    global xBola
    global zBola
    global score1
    global score2

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_MODELVIEW)
    
    # CAMPO
    draw_campo()
    # BOLA
    draw_bola()
    
    # TRAVE
    draw_barra_vertical(19,-0.8,5)
    draw_barra_vertical(19,-0.8,-5)
    draw_barra_vertical(-19,-0.8,5)  
    draw_barra_vertical(-19,-0.8,-5)
    draw_barra_horizontal(19,-1.3,0)
    draw_barra_horizontal(-19,-1.3,0)

    # LINHA CENTRAL
    bresenhamH(0,-6,0,6)

    # RETÂNGULO MENOR 1
    bresenhamH(7.5,-3,7.5,3)
    bresenhamV(7.5,-3,10,-3)
    bresenhamV(7.5,3,10,3)

    # RETÂNGULO MAIOR 1
    bresenhamH(6,-4,6,4)
    bresenhamV(6,-4,10,-4)
    bresenhamV(6,4,10,4)

    # RETÂNGULO MENOR 2
    bresenhamH(-7.5,-3,-7.5,3)
    bresenhamV(-10,-3,-7.5,-3)
    bresenhamV(-10,3,-7.5,3)

    # RETÂNGULO MAIOR 2
    bresenhamH(-6,-4,-6,4)
    bresenhamV(-10,-4,-6,-4)
    bresenhamV(-10,4,-6,4)

    circle(0,0,2)

    # PONTUAÇÃO
    if xBola >= 9.3 and zBola <= 1.78 and zBola >= -1.78:
        xBola = 0
        zBola = 0
        score1 = score1 + 1
        print('GOL!\n TIME 1: {}\nTIME 2: {}'.format(score1,score2))
    elif xBola <= -9.3 and zBola <= 1.78 and zBola >= -1.78:
        xBola = 0
        zBola = 0
        score2 = score2 + 1
        print('GOL!\nTIME 1: {}\nTIME 2: {}'.format(score1,score2))

    glutSwapBuffers()

def reshape(width, height):
    pass

def keyboard_handler(key, x, y):
    global eye
    global center
    global up
    global xBola
    global zBola

    # Movimentando a posição do observador (eye)
    if key == b"w":
        eye.z -= UNIT_PIXEL # Move uma unidade para frente

    elif key == b"s":
        eye.z += UNIT_PIXEL # Move uma unidade para trás

    elif key == b"d":
        eye.x += UNIT_PIXEL # Move uma unidade para direita

    elif key == b"a":
        eye.x -= UNIT_PIXEL # Move uma unidade para esquerda
    
    elif key == b"q":
        eye.y += UNIT_PIXEL # Move uma unidade para cima

    elif key == b"e":
        eye.y -= UNIT_PIXEL # Move uma unidade para baixo   

    # Movimentando a posição do ponto observado (center)
    elif key == b"i": # Código da seta para cima
        center.z -= UNIT_PIXEL # Move uma unidade para frente

    elif key == b"k": # Código da seta para baixo
        center.z += UNIT_PIXEL # Move uma unidade para trás

    elif key == b"l": # Código da seta pra direita
        center.x += UNIT_PIXEL # Move uma unidade para direita

    elif key == b"j": # Código da seta pra esquerda
        center.x -= UNIT_PIXEL # Move uma unidade para esquerda
    
    elif key == b"u": # Código da tecla page up
        center.y += UNIT_PIXEL # Move uma unidade para cima

    elif key == b"o": # Código da tecla page down
        center.y -= UNIT_PIXEL # Move uma unidade para baixo  

    # # Movimentando o vetor cima da câmera
    # elif key == b"f":
    #     if up.x != 0: # Se já estiver orientado no eixo x
    #         up.x *= -1   # Inverte a câmera
    #     else: 
    #         up.x = 1
        
    #     up.y = 0
    #     up.z = 0
    
    # elif key == b"g":
    #     if up.y != 0: # Se já estiver orientado no eixo y
    #         up.y *= -1   # Inverte a câmera
    #     else: 
    #         up.y = 1
        
    #     up.x = 0
    #     up.z = 0

    # elif key == b"h":
    #     if up.z != 0: # Se já estiver orientado no eixo z
    #         up.z *= -1   # Inverte a câmera
    #     else: 
    #         up.z = 1
        
    #     up.x = 0
    #     up.y = 0
    
    elif key == b't':
        xBola = xBola + 0.2
    elif key == b'g':
        xBola = xBola -0.2
    elif key == b'f':
        zBola = zBola -0.2
    elif key == b'h':
        zBola = zBola + 0.2
    elif key == b'r':
        xBola = xBola + 0.2
        zBola = zBola + 0.2
    elif key == b'y':
        xBola = xBola + 0.2
        zBola = zBola - 0.2
    elif key == b'v':
        xBola = xBola - 0.2
        zBola = zBola - 0.2
    elif key == b'b':
        xBola = xBola - 0.2
        zBola = zBola + 0.2

    update_camera()

    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH | GLUT_RGB)
glutInitWindowPosition(0,0)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)  
glutCreateWindow("Futebol")

init() 

glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard_handler)

glutMainLoop()
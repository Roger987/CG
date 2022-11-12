import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

textureCoordinates = ((0, 0), (0, 1), (1, 1), (1, 0))
texID = glGenTextures(2,[0,0])

surfaces = (
(0,1,2,3),
(3,2,7,6),
(6,7,5,4),
(4,5,1,0),
(1,5,7,2),
(4,0,3,6),
)

normals = [
( 0,  0, -1),  # surface 0
(-1,  0,  0),  # surface 1
( 0,  0,  1),  # surface 2
( 1,  0,  0),  # surface 3
( 0,  1,  0),  # surface 4
( 0, -1,  0)   # surface 5
    ]

colors = (
(1,1,1),
(0,1,0),
(0,0,1),
(0,1,0),
(0,0,1),
(1,0,1),
(0,1,0),
(1,0,1),
(0,1,0),
(0,0,1),
)

edges = (
(0,1),
(0,3),
(0,4),
(2,1),
(2,3),
(2,7),
(6,3),
(6,4),
(6,7),
(5,1),
(5,4),
(5,7),
)


def draw_campo(x,y,z):
    verticies = (
    ( x, -y, -z), # 0
    ( x,  y, -z), # 1
    (-x,  y, -z), # 2
    (-x, -y, -z), # 3
    ( x, -y,  z), # 4
    ( x,  y,  z), # 5
    (-x, -y,  z), # 6
    (-x,  y,  z), # 7
    )

    glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1, 1))
    glMaterialfv(GL_FRONT, GL_SHININESS, 1)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glEnable(GL_TEXTURE_2D)
    glShadeModel(GL_SMOOTH)

    image = pygame.image.load('grass.jpg')
    datas = pygame.image.tostring(image, 'RGBA')
    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, texID[0])
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, datas)
    glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT )
    glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT )
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)  
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

    glColor3fv([1,1,1])
    glBegin(GL_QUADS)
    for i_surface, surface in enumerate(surfaces):
        x = 0
        glNormal3fv(normals[i_surface])
        for i_vertex, vertex in enumerate(surface):
            x = x + 1
            
            glTexCoord2fv(textureCoordinates[i_vertex])
            glVertex3fv(verticies[vertex])
    glEnd()

    glDisable(GL_TEXTURE_2D)
    glColor3fv(colors[0])
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def draw_cube(x,y,z):

    verticies = (
    ( x, -y, -z), # 0
    ( x,  y, -z), # 1
    (-x,  y, -z), # 2
    (-x, -y, -z), # 3
    ( x, -y,  z), # 4
    ( x,  y,  z), # 5
    (-x, -y,  z), # 6
    (-x,  y,  z), # 7
    )

    glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1, 1))
    glMaterialfv(GL_FRONT, GL_SHININESS, 1)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    
    glEnable(GL_TEXTURE_2D)
    glShadeModel(GL_SMOOTH)

    image = pygame.image.load('cimento.jpg')
    datas = pygame.image.tostring(image, 'RGBA')
    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, texID[0])
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, datas)
    glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT )
    glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT )
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)


    glColor3fv([1, 1, 1])
    glBegin(GL_QUADS)
    for i_surface, surface in enumerate(surfaces):
        x = 0
        glNormal3fv(normals[i_surface])
        for i_vertex, vertex in enumerate(surface):
            x = x + 1
            
            glTexCoord2fv(textureCoordinates[i_vertex])
            glVertex3fv(verticies[vertex])
    glEnd()

    glDisable(GL_TEXTURE_2D)
    glColor3fv(colors[0])
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def draw_barra(x,y,z):

    verticies = (
    ( x, -y, -z), # 0
    ( x,  y, -z), # 1
    (-x,  y, -z), # 2
    (-x, -y, -z), # 3
    ( x, -y,  z), # 4
    ( x,  y,  z), # 5
    (-x, -y,  z), # 6
    (-x,  y,  z), # 7
    )

    glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1, 1))
    glMaterialfv(GL_FRONT, GL_SHININESS, 1)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glEnable(GL_TEXTURE_2D)
    glShadeModel(GL_SMOOTH)

    image = pygame.image.load('metal.jpg')
    datas = pygame.image.tostring(image, 'RGBA')
    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, texID[0])
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, datas)
    glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT )
    glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT )
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)


    glColor3fv([1, 1, 1])
    glBegin(GL_QUADS)
    for i_surface, surface in enumerate(surfaces):
        x = 0
        glNormal3fv(normals[i_surface])
        for i_vertex, vertex in enumerate(surface):
            x = x + 1
            
            glTexCoord2fv(textureCoordinates[i_vertex])
            glVertex3fv(verticies[vertex])
    glEnd()

    glColor3fv(colors[0])
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
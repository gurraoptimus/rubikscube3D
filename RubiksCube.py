import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Definiera färger för kubens sidor
COLORS = {
    'white': (1, 1, 1),
    'yellow': (1, 1, 0),
    'green': (0, 1, 0),
    'blue': (0, 0, 1),
    'orange': (1, 0.5, 0),
    'red': (1, 0, 0)
}

# Skapa kubens ytor och färger
def create_cube():
    vertices = [
        (1, 1, -1), (1, -1, -1), (-1, -1, -1), (-1, 1, -1),
        (1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1)
    ]
    
    edges = (
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    )
    
    surfaces = (
        (0, 1, 2, 3), (3, 2, 6, 7), (6, 7, 4, 5),
        (4, 5, 1, 0), (1, 5, 6, 2), (4, 0, 3, 7)
    )
    
    surface_colors = [
        COLORS['white'], COLORS['yellow'], COLORS['green'],
        COLORS['blue'], COLORS['orange'], COLORS['red']
    ]
    
    return vertices, edges, surfaces, surface_colors

# Ritar kuben med OpenGL
def draw_cube(vertices, edges, surfaces, surface_colors):
    glBegin(GL_QUADS)
    for i, surface in enumerate(surfaces):
        glColor3fv(surface_colors[i])
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()
    
    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Skapa fönstret med Pygame och OpenGL
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    
    vertices, edges, surfaces, surface_colors = create_cube()
    
    # Loop för att hantera inmatning och uppdatera skärmen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # Tillämpa rotation för att simulera kubens rörelse
        glRotatef(1, 3, 1, 1)
        
        # Rensa och rita kuben
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube(vertices, edges, surfaces, surface_colors)
        pygame.display.flip()
        pygame.time.wait(10)

# Kör programmet
if __name__ == "__main__":
    main()

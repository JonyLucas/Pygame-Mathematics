import pygame
from pygame.locals import *
from OpenGL.GL import *

pygame.init()
pygame.display.set_mode((500, 500), DOUBLEBUF | OPENGL) # Use double buffer and OpenGL, one for drawing, one for displaying
pygame.display.set_caption('OpenGL')

done = False
white = pygame.Color(255, 255, 255)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear the screen
    pygame.display.flip() # Swap buffers

pygame.quit()
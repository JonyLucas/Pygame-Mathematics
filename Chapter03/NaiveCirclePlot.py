import math
import pygame

pygame.init()

screen_width = 400
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Naive Circle Plot")

done = False
white = pygame.Color(255, 255, 255)
radius = 50
center = (screen_width // 2, screen_height // 2)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for x in range(-50,50):
        y = math.sqrt(radius**2 - x**2)
        screen.set_at((x + center[0], int(y) + center[1]), white)
        screen.set_at((x + center[0], -int(y) + center[1]), white)
        # screen.set_at((int(y) + center[0], x + center[1]), white)
        # screen.set_at((-int(y) + center[0], x + center[1]), white)
    pygame.display.update()

pygame.quit()
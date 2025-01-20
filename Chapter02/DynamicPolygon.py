import pygame
from pygame.locals import * # Getting user inputs

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

done = False
times_clicked = 0
point1 = 0
point2 = 0
point3 = 0
lines = []
polygons = []

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        else:
            if event.type == MOUSEBUTTONDOWN:
                if times_clicked == 0:
                    point1 = pygame.mouse.get_pos()
                    times_clicked += 1
                elif times_clicked == 1:
                    point2 = pygame.mouse.get_pos()
                    lines.append((point1, point2))
                    times_clicked += 1
                else:
                    point3 = pygame.mouse.get_pos()
                    lines.clear()
                    polygons.append((point1, point2, point3))
                    times_clicked = 0

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen_width, screen_height))
    if times_clicked == 1:
        point2 = pygame.mouse.get_pos()
        pygame.draw.line(screen, (255, 255, 255), point1, point2)
    elif times_clicked == 2:
        point3 = pygame.mouse.get_pos()
        pygame.draw.line(screen, (255, 255, 255), point2, point3)
        pygame.draw.line(screen, (255, 255, 255), point3, point1)

    for line in lines:
        pygame.draw.line(screen, (255, 255, 255), line[0], line[1])

    for polygon in polygons:
        pygame.draw.polygon(screen, (255, 255, 255), polygon)

    pygame.display.update()

pygame.quit()
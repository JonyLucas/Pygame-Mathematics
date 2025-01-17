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
lines = []

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        else:
            if event.type == MOUSEBUTTONDOWN:
                if times_clicked == 0:
                    point1 = pygame.mouse.get_pos()
                    times_clicked += 1
                else:
                    point2 = pygame.mouse.get_pos()
                    lines.append((point1, point2))
                    times_clicked = 0

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen_width, screen_height))
    if times_clicked == 1:
        point2 = pygame.mouse.get_pos()
        pygame.draw.line(screen, (255, 255, 255), point1, point2)

    for line in lines:
        pygame.draw.line(screen, (255, 255, 255), line[0], line[1])

    pygame.display.update()

pygame.quit()
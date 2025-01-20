import pygame

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
white = pygame.Color(255, 255, 255)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.polygon(screen, white, [(100, 100), (400, 100), (200, 300)])
    pygame.display.update()

pygame.quit()
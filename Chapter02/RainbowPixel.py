import pygame

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for x in range(screen_width):
        for y in range(screen_height):
            screen.set_at((x, y), pygame.Color(int(255 * x / screen_width), int(255 * y / screen_height), 255))

    pygame.display.update()

pygame.quit()
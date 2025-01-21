import pygame

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)

xoriginoffset = screen_width // 2
yoriginoffset = screen_height // 2

def invert_y(y):
    return screen_height - y

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # draw x axis
    for x in range(-500, 500):
        screen.set_at((x + xoriginoffset, yoriginoffset), green)

    # draw y axis
    for y in range(-400, 400):
        screen.set_at((xoriginoffset, y + yoriginoffset), green)

    for x in range(-500, 500):
        # line equation
        # y = 2 * x + 4
        # y = int(0.05 * x) - 100
        y = 10 * x -100
        screen.set_at((x + xoriginoffset, invert_y(y + yoriginoffset)), white)

    pygame.display.update()

pygame.quit()
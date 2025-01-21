import pygame

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
times_clicked = 0
point1 = (0, 0)
point2 = (0, 0)

def plot_line(point1, point2):
    x0, y0 = point1
    x1, y1 = point2
    m = (y1 - y0) / (x1 - x0)
    c = y0 - m * x0
    if x0 > x1:
        x0, x1 = x1, x0
    for x in range(x0, x1):
        y = m * x + c # line equation
        screen.set_at((int(x), int(y)), white)

def breseham_line(point1, point2):
    x0, y0 = point1
    x1, y1 = point2
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy

    while True:
        screen.set_at((x0, y0), white)
        if x0 == x1 and y0 == y1:
            break

        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if times_clicked == 0:
                point1 = event.pos
                times_clicked += 1
            elif times_clicked == 1:
                point2 = event.pos
                # pygame.draw.line(screen, white, point1, point2)
                # plot_line(point1, point2)
                breseham_line(point1, point2)
                times_clicked = 0

    pygame.display.update()

pygame.quit()
import random

import pygame

class Rect:
    def __init__(self, x_pos, y_pos, min_size, max_size, delta):
        self.is_increasing = True
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = min_size
        self.min_width = min_size
        self.max_width = max_size
        self.height = min_size
        self.min_height = min_size
        self.max_height = max_size
        self.delta = delta

    def update(self, screen_ref, color):
        if self.is_increasing:
            self.width += self.delta
            self.height += self.delta
            if self.width >= self.max_width or self.height >= self.max_height:
                self.is_increasing = False
        else:
            self.width -= self.delta
            self.height -= self.delta
            if self.width <= self.min_width or self.height <= self.min_height:
                self.is_increasing = True

        pygame.draw.rect(screen_ref, color, (self.x_pos, self.y_pos, self.width, self.height))


pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)
max_delta = 0.01

rects = [
    Rect(random.random() * screen_width, random.random() * screen_height, 10, 50, random.random() * max_delta),
    Rect(random.random() * screen_width, random.random() * screen_height, 10, 30, random.random() * max_delta),
    Rect(random.random() * screen_width, random.random() * screen_height, 10, 50, random.random() * max_delta),
    Rect(random.random() * screen_width, random.random() * screen_height, 10, 25, random.random() * max_delta),
    Rect(random.random() * screen_width, random.random() * screen_height, 10, 50, random.random() * max_delta),
    Rect(random.random() * screen_width, random.random() * screen_height, 10, 10, random.random() * max_delta),
    Rect(random.random() * screen_width, random.random() * screen_height, 10, 60, random.random() * max_delta),
]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen_width, screen_height))
    for rect in rects:
        rect.update(screen, white)
    # pygame.draw.rect(screen, white, (300, 300, 50, 50)) # Draw a rectangle at (300,300) with width 50 and height 50
    pygame.display.update()

pygame.quit()
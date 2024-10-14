import pygame

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.set_at((100,100), white) # Set a pixel at (100,100) to white
    screen.set_at((200,200), white) # Set a pixel at (200,200) to white

    pygame.draw.rect(screen, white, (300, 300, 50, 50)) # Draw a rectangle at (300,300) with width 50 and height 50
    pygame.display.update()

pygame.quit()
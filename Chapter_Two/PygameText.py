import pygame

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.font.init()
print(pygame.font.get_fonts())
font = pygame.font.SysFont('Comic Sans MS', 120, True, False)
text = font.render('Hello World', False, (255, 255, 255))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(text, (100, 100))
    pygame.display.update()

pygame.quit()
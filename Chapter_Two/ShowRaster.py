import pygame

pygame.init()

screen_width = 1000
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Show Image")

background = pygame.image.load("../images/SceneCapture.png")
sprite = pygame.image.load("../images/RobotAvatar.png")

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background, (0, 0))
    screen.blit(sprite, (300, 200))
    pygame.display.update()

pygame.quit()
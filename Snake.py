import pygame

# Essentials
pygame.init()
pygame.display.set_caption("Snake Game")
size = SW, SH = 1280, 720
screen = pygame.display.set_mode(size)

# Variables
BLOCK_SIZE = 30
running = True

clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)


pygame.quit()
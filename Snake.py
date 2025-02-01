import pygame

# Essentials
pygame.init()
pygame.display.set_caption("Snake Game")
size = SW, SH = 800, 600
screen = pygame.display.set_mode(size)

# Variables
BLOCK_SIZE = 50
running = True

clock = pygame.time.Clock()


# Creating the Snake Object
class Snake:
    def __init__(self):
        self.x = BLOCK_SIZE
        self.y = BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False



# Creating grid of the map
def snake_map():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)

snake_map()

snake = Snake()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.draw.rect(screen, "blue", snake.head)
    
    for square in snake.body:
        pygame.draw.rect(screen, "green", square)
    
    pygame.display.update()
    clock.tick(10)
    

pygame.quit()
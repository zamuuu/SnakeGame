import pygame
from random import randint
import sys
# Essentials
pygame.init()
pygame.display.set_caption("Snake Game")
size = SW, SH = 800, 600
screen = pygame.display.set_mode(size)

# Variables
FONT = pygame.font.SysFont("Arial", 50)
BLOCK_SIZE = 50
main_menu_BG = pygame.image.load('imgs/Background.png')
# game_BG = pygame.image.load("#")
clock = pygame.time.Clock()

# Creating the Snake Object
class Snake:
    def __init__(self):
        # Position of the snake
        self.x = BLOCK_SIZE
        self.y = BLOCK_SIZE
        # Direction of the snake. 1 -> Right ; -1 -> Left ; 0 -> Static
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self):
        global apple
        for square in self.body:
            if (self.head.x, self.head.y) == (square.x, square.y):
                self.dead = True
            if self.head.x not in range(0, SW) or self.head.y not in range(0, SH):
                self.dead = True
        
        
        if self.dead:
            self.x = BLOCK_SIZE
            self.y = BLOCK_SIZE
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
            self.xdir = 1
            self.ydir = 0
            self.dead = False
            apple = Apple()
            
            
            
            
        self.body.append(self.head)
        for i in range(len(self.body)-1):
            # Move each body rect to the the position of the next one
            self.body[i].x = self.body[i+1].x 
            self.body[i].y = self.body[i+1].y 
        # Move head position to the next BLOCK of the direction of the head 
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)

# Creating the Apple Object
class Apple:
    def __init__(self):
        self.x = int(randint(0, SW)/BLOCK_SIZE) * BLOCK_SIZE 
        self.y = int(randint(0, SH)/BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update(self):
        pygame.draw.rect(screen, "#ff0000", self.rect)

# Creating grid of the map
def snake_map():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)


def main_menu():
    pygame.display.set_caption("Main Menu")
    click = False
    while True:
        # Main menu Background image
        screen.blit(main_menu_BG, (0,0))
        
        mousex, mousey = pygame.mouse.get_pos()
        # Button to enter the game
        game_button = pygame.Rect(0, 0, 400, 100)
        # Centering the Play button
        game_button.center = (SW // 2, SH // 2)
        #game_button = game_button.center
        if game_button.collidepoint(mousex,mousey):
            
            if click:
                game()
                
        pygame.draw.rect(screen, (255,0,255), game_button)
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(20)
                



def game():
    pygame.display.set_caption("Snake!")
    running = True
    # Initialize map Grid, Snake and Apple
    snake_map()
    snake = Snake()
    apple = Apple()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False
               sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    main_menu()
                    
            # Movement with Arrows and a,w,s,d keys.
            if event.type == pygame.KEYDOWN:
                if event.key in {pygame.K_DOWN, pygame.K_s}:
                    if snake.ydir == -1:
                        pass
                    else:
                        snake.xdir, snake.ydir = 0, 1
                elif event.key in {pygame.K_LEFT, pygame.K_a}:
                    if snake.xdir == 1:
                        pass
                    else:
                        snake.xdir, snake.ydir = -1, 0
                elif event.key in {pygame.K_UP, pygame.K_w}:
                    if snake.ydir == 1:
                        pass
                    else:
                        snake.xdir, snake.ydir = 0, -1
                elif event.key in {pygame.K_RIGHT, pygame.K_d}:
                    if snake.xdir == -1:
                        pass
                    else:
                        snake.xdir, snake.ydir = 1, 0


        screen.fill("black")
        snake_map()
        snake.update()
        apple.update()



        pygame.draw.rect(screen, "#2461ff", snake.head)    
        for square in snake.body:
            pygame.draw.rect(screen, "#4775eb", square)    

        if (snake.head.x, snake.head.y) == (apple.x, apple.y):
            snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
            apple = Apple()

        pygame.display.update()
        clock.tick(10)

main_menu()
pygame.quit()
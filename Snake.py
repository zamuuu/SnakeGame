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
clock = pygame.time.Clock()
# Imgages
main_menu_BG = pygame.image.load('imgs/main_menu_background.png').convert_alpha()
game_BG = pygame.image.load("imgs/game_background.jpg").convert_alpha()
play_main_menu = pygame.image.load("imgs/play_button.png").convert_alpha()
# Change difficulty images
easy_difficulty = pygame.image.load("imgs/turtle.png").convert_alpha()
normal_difficulty = pygame.image.load("imgs/rabbit.png").convert_alpha()
hard_difficulty = pygame.image.load("imgs/snake.png").convert_alpha()
clicked_easy_diff = pygame.image.load("imgs/turtle_clicked.png").convert_alpha()
clicked_normal_diff = pygame.image.load("imgs/rabbit_clicked.png").convert_alpha()
clicked_hard_diff = pygame.image.load("imgs/snake_clicked.png").convert_alpha()
temp_blank = pygame.image.load("imgs/blank_temporary.png").convert_alpha()
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
        self.x = randint(0, (SW // BLOCK_SIZE) - 1) * BLOCK_SIZE
        self.y = randint(0, (SH // BLOCK_SIZE) - 1) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update(self):
        pygame.draw.rect(screen, "#ff0000", self.rect)


def main_menu():
    selected_difficulty = 10  # Valor por defecto
    pygame.display.set_caption("Main Menu")
    click = False
    which_diff = temp_blank
    difficulty_posx = 0
    difficulty_posy = 0
    while True:
        # Main menu Background image
        screen.blit(main_menu_BG, (0,0))
        mousex, mousey = pygame.mouse.get_pos()

        # Play button
        play_main_menu_rect = play_main_menu.get_rect()
        play_main_menu_rect.center = (SW // 2, SH // 2)
        
        # Difficulty Rect buttons
        easy_dificulty_r = easy_difficulty.get_rect()
        normal_dificulty_r = normal_difficulty.get_rect()
        hard_dificulty_r = hard_difficulty.get_rect()
        
        # Positioning those bottons
        easy_dificulty_r.topleft = (200, 380)
        normal_dificulty_r.topleft = (350, 380)
        hard_dificulty_r.topleft = (500, 380)
        
        
        screen.blit(play_main_menu, play_main_menu_rect)
        screen.blit(easy_difficulty, (200, 380))
        screen.blit(normal_difficulty, (350, 380))
        screen.blit(hard_difficulty, (500, 380))
        
        
        if play_main_menu_rect.collidepoint(mousex, mousey) and click:
            game(selected_difficulty)
        elif easy_dificulty_r.collidepoint(mousex, mousey) and click:
            selected_difficulty = 6
            which_diff = clicked_easy_diff
            difficulty_posx, difficulty_posy = 200, 380
        elif normal_dificulty_r.collidepoint(mousex, mousey) and click:
            selected_difficulty = 10
            which_diff = clicked_normal_diff
            difficulty_posx, difficulty_posy = 350, 380
        elif hard_dificulty_r.collidepoint(mousex, mousey) and click:
            selected_difficulty = 20
            which_diff = clicked_hard_diff
            difficulty_posx, difficulty_posy = 500, 380
        click = False
        
        screen.blit(which_diff, (difficulty_posx,difficulty_posy))
        
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
        
        clock.tick(60)
                



def game(selected_difficulty):
    pygame.display.set_caption("Snake!")
    running = True
    # Initialize map Grid, Snake and Apple
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

        screen.blit(game_BG, (0,0))
        snake.update()
        apple.update()



        pygame.draw.rect(screen, "#2461ff", snake.head)    
        for square in snake.body:
            pygame.draw.rect(screen, "#4775eb", square)    

        if (snake.head.x, snake.head.y) == (apple.x, apple.y):
            snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
            apple = Apple()
            apple.update()

        pygame.display.update()
        clock.tick(selected_difficulty)

main_menu()
pygame.quit()
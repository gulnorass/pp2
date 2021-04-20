import pygame
import random 
import time

pygame.init()

WIDTH = 600
HEIGHT = 500

go = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Snake Game')
font = pygame.font.SysFont('Arial', 30)

FPS = 30
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.size = 3
        self.radius = 10
        self.dx = 5
        self.dy = 0
        self.elements = [[100, 100], [120, 100], [140, 100]]
        self.score = 0
        self.is_add = False

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (50, 28, 217), element, self.radius)

    def add_snake(self):
        self.size += 1
        self.score += 1
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_snake()
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]
        
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

class Food:
    def __init__(self):
        self.x = random.randint(100, WIDTH - 70)
        self.y = random.randint(100, HEIGHT - 70)
        self.image = pygame.image.load("apple.png")
        # self.position = [random.randint(0, WIDTH - 100), random.randint(0, HEIGHT - 100)]
    
    def draw(self):
        screen.blit(self.image, (self.x, self.y))

def show_score(x, y, score):
    show = font.render('Score: ' + str(score), True, (50, 28, 217))
    screen.blit(show, (x, y))

def collision():
    if(food.x in range(snake.elements[0][0] - 20, snake.elements[0][0])) and (food.y in range(snake.elements[0][1] - 20, snake.elements[0][1])):
        snake.is_add = True
        food.x = random.randint(50, WIDTH - 70)
        food.y = random.randint(50, HEIGHT - 70)
    if(food.x in range(snake2.elements[0][0] - 20, snake2.elements[0][0])) and (food.y in range(snake2.elements[0][1] - 20, snake2.elements[0][1])):
        snake2.is_add = True
        food.x = random.randint(50, WIDTH - 70)
        food.y = random.randint(50, HEIGHT - 70)

def is_in_walls():
    return snake.elements[0][0] > WIDTH - 25 or snake.elements[0][0] < 30
def is_in_walls2():
    return snake2.elements[0][0] > WIDTH - 25 or snake2.elements[0][0] < 30

def game_over():
    # pygame.display.flip()
    screen.fill((255, 0, 0))
    txt = font.render('GAME OVER!', True, (255, 255, 255))
    my_score = font.render('Total score1: ' + str(snake.score), True, (255, 255, 255))
    my_score2 = font.render('Total score2: ' + str(snake2.score), True, (255, 255, 255))
    screen.blit(txt, (200, 200))
    screen.blit(my_score, (200, 300))
    screen.blit(my_score2, (200, 350))
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()

def show_walls():
    for i in range(0, WIDTH, 15):
        screen.blit(wall_image, (i, 0))
        screen.blit(wall_image, (i, HEIGHT - 32))
        screen.blit(wall_image, (0, i))
        screen.blit(wall_image, (WIDTH - 32, i))

snake = Snake()
snake2 = Snake()
go = True
food = Food()
d=5

wall_image = pygame.image.load('wall.png')


while go:
    mil = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                go = False
            if event.key == pygame.K_RIGHT and snake.dx != -d:
                snake.dx = d
                snake.dy = 0
            if event.key == pygame.K_LEFT and snake.dx != d:
                snake.dx = -d
                snake.dy = 0
            if event.key == pygame.K_UP and snake.dy != d:
                snake.dx = 0
                snake.dy = -d
            if event.key == pygame.K_DOWN and snake.dy != -d:
                snake.dx = 0
                snake.dy = d

            if event.key == pygame.K_d and snake2.dx != -d:
                snake2.dx = d
                snake2.dy = 0
            if event.key == pygame.K_a and snake2.dx != d:
                snake2.dx = -d
                snake2.dy = 0
            if event.key == pygame.K_w and snake2.dy != d:
                snake2.dx = 0
                snake2.dy = -d
            if event.key == pygame.K_s and snake2.dy != -d:
                snake2.dx = 0
                snake2.dy = d
    
    if is_in_walls():
        game_over()
        go = False
    if is_in_walls2():
        game_over()
        go = False

    collision()
    screen.fill((165, 206, 216))
    snake.move()
    snake.draw()
    snake2.move()
    snake2.draw()
    food.draw()
    show_score(35, 45, snake.score)
    show_score(450, 45, snake2.score)
    show_walls()
    pygame.display.flip()
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up game variables
block_size = 10
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

# Define functions
def draw_snake(snake_list):
    for x,y in snake_list:
        pygame.draw.rect(screen, BLACK, [x, y, block_size, block_size])

def message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [screen_width/6, screen_height/3])

# Define the game loop
def gameLoop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    # Create the food
    foodx = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0

    snake_list = []
    Length_of_snake: int = 1

    # Game loop
    while not game_over:

        while game_close == True:
            screen.fill(WHITE)
            message("You lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Check for collision with wall or self
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        for segment in snake_list[1:]:
            if segment == [x1, y1]:
                game_close = True

        # Move the snake
        x1 += x1_change
        y1 += y1_change

        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, [foodx, foody, block_size, block_size])

        # Add new segment to snake
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > Length_of_snake: del snake_list[0]
    # Draw the snake
    draw_snake(snake_list)

    # Update the display
    pygame.display.update()

    # Check if the snake has collided with the food
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
        foody = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0
        Length_of_snake += 1

    # Set the clock tick
    clock.tick(20)

# Quit Pygame
pygame.quit()
quit()

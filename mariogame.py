import pygame

pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mario Game")

# Create Mario character
mario_image = pygame.image.load('mario.png')
mario_x = 400
mario_y = 500

# Add obstacles
obstacle_image = pygame.image.load('obstacle.png')
obstacle_x = 200
obstacle_y = 500

# Add scoring system
score = 0
font = pygame.font.Font(None, 36)

# Define game mechanics
jumping = False
jump_count = 10
speed = 5

# Define game rules
game_over = False

# Game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jumping = True

    # Move Mario
    if jumping:
        mario_y -= jump_count
        jump_count -= 1
        if jump_count < 0:
            jumping = False
            jump_count = 10
    else:
        mario_y += speed

    # Check for collision
    if mario_x + 50 > obstacle_x and mario_x < obstacle_x + 50 and mario_y + 50 > obstacle_y and mario_y < obstacle_y + 50:
        game_over = True

    # Update score
    score += 1

    # Draw the screen
    screen.fill((255, 255, 255))
    screen.blit(mario_image, (mario_x, mario_y))
    screen.blit(obstacle_image, (obstacle_x, obstacle_y))
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.update()

pygame.quit()

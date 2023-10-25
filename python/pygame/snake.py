import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up display dimensions
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake initial position
x, y = WIDTH // 2, HEIGHT // 2
snake = [(x, y)]
snake_direction = "RIGHT"
snake_length = 1

# Food initial position
food_x, food_y = random.randrange(0, WIDTH - 10, 10), random.randrange(0, HEIGHT - 10, 10)

# Set up game clock
clock = pygame.time.Clock()

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(win, GREEN, (segment[0], segment[1], 10, 10))

def draw_food(food_x, food_y):
    pygame.draw.rect(win, RED, (food_x, food_y, 10, 10))

def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    win.blit(text, text_rect)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Change snake direction with arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"

    # Move the snake
    if snake_direction == "LEFT":
        x -= 10
    if snake_direction == "RIGHT":
        x += 10
    if snake_direction == "UP":
        y -= 10
    if snake_direction == "DOWN":
        y += 10

    # Check for collisions
    if x == food_x and y == food_y:
        snake_length += 1
        food_x, food_y = random.randrange(0, WIDTH - 10, 10), random.randrange(0, HEIGHT - 10, 10)

    snake.append((x, y))

    # Remove the tail if the snake is too long
    if len(snake) > snake_length:
        del snake[0]

    # Check if snake hits the wall
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        game_over()

    # Check if snake collides with itself
    if (x, y) in snake[:-1]:
        game_over()

    win.fill(BLACK)
    draw_snake(snake)
    draw_food(food_x, food_y)
    pygame.display.update()
    clock.tick(20)

# Quit Pygame
pygame.quit()
quit()

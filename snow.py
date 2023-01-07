import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the window title
pygame.display.set_caption("Snowflake Fall")

# Set the snowflake image
snowflake_image = pygame.image.load("snowflake.png")

# Create a list to store the snowflakes
snowflakes = []

while True:
    # Fill the background with black
    screen.fill((0, 0, 0))

    # Generate a new snowflake at a random position
    x = random.randint(0, window_size[0] - snowflake_image.get_width())
    y = 0
    snowflakes.append((x, y))

    # Draw the snowflakes
    for x, y in snowflakes:
        screen.blit(snowflake_image, (x, y))

    # Update the snowflake positions
    snowflakes = [(x, y + 1) for x, y in snowflakes]

    # Remove the snowflakes that have fallen off the bottom of the screen
    snowflakes = [(x, y) for x, y in snowflakes if y < window_size[1]]

    # Update the display
    pygame.display.flip()

    # Sleep for 1/60th of a second
    pygame.time.wait(1000 // 60)

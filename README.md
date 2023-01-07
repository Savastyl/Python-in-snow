# Python in snow

Python script that will display a snowflake falling using the Pygame library.

![Alt text](Media/Screenshot%202023-01-07%20024124.png)

```
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

    ```


The script will display a snowflake falling using Pygame, a library for creating games and graphical applications in Python.
It will run an infinite loop that generates a new snowflake at a random position on the top of the screen, draws the snowflakes
on the screen, and updates their positions by moving them down one pixel per frame. It will also remove any snowflakes that have
fallen off the bottom of the screen.

To run the script, you will need to have Pygame installed. You can install Pygame using pip:

```
pip install pygame

```

You will also need to have a snowflake image file named 'snowflake.png' in the same directory as the script. You can create your own
snowflake image or use one from the internet.

Then, save the script to a file with a '.py' extension and run it using the Python interpreter. For example, if you save the file as
'snowflake_fall.py', you can run it like this:

```
python snowflake_fall.py

```

This will execute the script and display a window with snowflakes falling from the top of the screen.





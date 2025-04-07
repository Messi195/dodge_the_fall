import pygame
import sys
import random
from pygame.locals import QUIT, K_LEFT, K_RIGHT

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge!")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Game settings
FPS = 60
clock = pygame.time.Clock()

# Player settings
player_width, player_height = 50, 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 6

# Obstacle settings
square_width, square_height = 50, 50
square_x = random.randint(0, WIDTH - square_width)
square_y = -square_height
square_speed = 20

def handle_events() -> None:
    """Handles all events in the game loop (quit and key presses)."""
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def move_player(keys: pygame.key.ScancodeWrapper) -> None:
    """Moves the player left or right based on key input."""
    global player_x
    if keys[K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

def update_obstacle() -> None:
    """Moves the falling obstacle and resets it if it goes off-screen."""
    global square_x, square_y
    square_y += square_speed
    if square_y > HEIGHT:
        square_x = random.randint(0, WIDTH - square_width)
        square_y = -square_height

def check_collision() -> bool:
    """Checks if the player and obstacle have collided."""
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    square_rect = pygame.Rect(square_x, square_y, square_width, square_height)
    return player_rect.colliderect(square_rect)

def draw_objects() -> None:
    """Draws the player and the obstacle on the screen."""
    screen.fill(BLACK)
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    square_rect = pygame.Rect(square_x, square_y, square_width, square_height)
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, square_rect)

def game_loop() -> None:
    """Main game loop."""
    while True:
        handle_events()

        keys = pygame.key.get_pressed()
        move_player(keys)
        update_obstacle()

        if check_collision():
            print("YOU LOSE")
            pygame.quit()
            sys.exit()

        draw_objects()

        pygame.display.flip()
        clock.tick(FPS)

# Start the game
game_loop()

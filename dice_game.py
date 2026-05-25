import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# Dice settings
dice_number = 1
dice_size = 150
dice_x = 125
dice_y = 100

running = True

def draw_dice(number):
    # Draw dice box
    pygame.draw.rect(screen, WHITE, (dice_x, dice_y, dice_size, dice_size))
    pygame.draw.rect(screen, BLACK, (dice_x, dice_y, dice_size, dice_size), 3)

    # Dot positions
    left = dice_x + 35
    center_x = dice_x + 75
    right = dice_x + 115

    top = dice_y + 35
    center_y = dice_y + 75
    bottom = dice_y + 115

    radius = 8

    dots = {
        1: [(center_x, center_y)],

        2: [(left, top), (right, bottom)],

        3: [(left, top), (center_x, center_y), (right, bottom)],

        4: [(left, top), (right, top),
            (left, bottom), (right, bottom)],

        5: [(left, top), (right, top),
            (center_x, center_y),
            (left, bottom), (right, bottom)],

        6: [(left, top), (right, top),
            (left, center_y), (right, center_y),
            (left, bottom), (right, bottom)]
    }

    # Draw dots
    for pos in dots[number]:
        pygame.draw.circle(screen, BLACK, pos, radius)


while running:

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Press SPACE to roll dice
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice_number = random.randint(1, 6)

    # Background
    screen.fill((200, 200, 200))

    # Draw dice
    draw_dice(dice_number)

    # Instructions
    font = pygame.font.Font(None, 36)
    text = font.render("Press SPACE to Roll", True, BLACK)
    screen.blit(text, (80, 300))

    # Update display
    pygame.display.update()

    # FPS
    clock.tick(60)

pygame.quit()
sys.exit()
"""
First / main copy
"""

import pygame

scoreA = 0
scoreB = 0

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (254, 87, 236)
YELLOW = (253, 229, 33)
DARKGREEN = (86, 166, 34)
CIRCLE_RADIUS = 10

pygame.init()

# Set the height and width of the screen.
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("PONG")

# Loop until the user clicks the close button.
carryOn = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of the rectangle

ball_posx = 50
ball_posy = 50
ball_posx2 = 50
ball_posy2 = 50
ball_posx3 = 50
ball_posy3 = 50
PADDLE1_x4 = 30
PADDLE1_y4 = 200
PADDLE2_x5 = 675
PADDLE2_y5 = 200
rect_x7 = 340
rect_y7 = 0
ball_posx4 = 340
ball_posy4 = 225
paddlehit_x = PADDLE1_x4 + 10

# Speed and direction of rectangle
ball_change_posx = 5
ball_change_posy = 5
ball_change_posx2 = 4
ball_change_posy2 = 4
ball_change_posx3 = 3
ball_change_posy3 = 3
step = 5

pixel = [1, 1]

# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)

# -------- Main Program Loop -----------
while carryOn:

    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                carryOn = False
    # informing what occur for game over (main operation) before what occurs before/without game over

    # Only move and process game logic if the game isn't over.
    if carryOn:
        # Move the rectangle starting point
        ball_posx += ball_change_posx
        ball_posy += ball_change_posy
        ball_posx2 += ball_change_posx2
        ball_posy2 += ball_change_posy2
        ball_posx3 += ball_change_posx3
        ball_posy3 += ball_change_posy3
        # Bounce the ball if needed
        if ball_posy > 450 or ball_posy < 0:
            ball_change_posy = ball_change_posy * -1
        if ball_posx > 700 or ball_posx < 0:
            ball_change_posx = ball_change_posx * -1
        if ball_posy2 > 450 or ball_posy2 < 0:
            ball_change_posy2 = ball_change_posy2 * -1
        if ball_posx2 > 700 or ball_posx2 < 0:
            ball_change_posx2 = ball_change_posx2 * -1
        if ball_posy3 > 450 or ball_posy3 < 0:
            ball_change_posy3 = ball_change_posy3 * -1
        if ball_posx3 > 700 or ball_posx3 < 0:
            ball_change_posx3 = ball_change_posx3 * -1
        if ball_posx >= 703:
            scoreB += 1
        if ball_posx <= -3:
            scoreA += 1
        if ball_posx2 >= 700:
            scoreB += 1
        if ball_posx2 <= 0:
            scoreA += 1
        if ball_posx3 >= 700:
            scoreB += 1
        if ball_posx3 <= 0:
            scoreA += 1
        if (ball_posy > PADDLE1_y4) and (ball_posy < PADDLE1_y4 + 70):
            if ball_posx <= PADDLE1_x4 + 10:
                ball_change_posx = ball_change_posx * -1

        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_UP]:
            if PADDLE2_y5 > 0:
                PADDLE2_y5 -= step
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_DOWN]:
            if PADDLE2_y5 < 427:
                PADDLE2_y5 += step
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_w]:
            if PADDLE1_y4 > 0:
                PADDLE1_y4 -= step
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_s]:
            if PADDLE1_y4 < 427:
                PADDLE1_y4 += step

    # setting the scene

    # Set the screen background
    screen.fill(DARKGREEN)

    # Draw the rectangle
    pygame.draw.circle(screen, PINK, [ball_posx, ball_posy], CIRCLE_RADIUS)
    pygame.draw.circle(screen, WHITE, [ball_posx2, ball_posy2], CIRCLE_RADIUS)
    pygame.draw.circle(screen, WHITE, [ball_posx3, ball_posy3], CIRCLE_RADIUS)
    pygame.draw.rect(screen, WHITE, [PADDLE1_x4, PADDLE1_y4, 10, 70])
    pygame.draw.rect(screen, WHITE, [PADDLE2_x5, PADDLE2_y5, 10, 70])
    pygame.draw.rect(screen, WHITE, [rect_x7, rect_y7, 5, 1000])
    pygame.draw.circle(screen, WHITE, [ball_posx4, ball_posy4], 60, 6)

    font = pygame.font.Font(None, 60)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))

    # Limit frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

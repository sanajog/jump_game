# Aim:- Jump Game
import pygame
import math
import random

# Game Variables
HEIGHT = 600
WIDTH = 800
BLACK = (0, 0, 0)
W = (255, 255, 255)
# Initialize pygame
pygame.init()

# Make the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump Game Made By 210186")

# Make the background
background = pygame.image.load("back.png")

# Make the icon
icon = pygame.image.load("gg.png")
pygame.display.set_icon(icon)

# Make the player
playerImg = pygame.image.load("char.png")

playerX = 400
playerY = 10
playerX_change = 0
playerY_change = 5

# Make the platform
platformImg = []
platformX = []
platformY = []
num_of_platforms = 4

for i in range(num_of_platforms):
    platformImg.append(pygame.image.load("barr.png"))

    platformX.append(random.randint(0, 690))
    platformY.append(random.randint(60, 500))

# Make the scoring system
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32, fg="white")
textX = 10
textY = 10


# Functions
def player(x, y):
    screen.blit(playerImg, (x, y))


def platform(x, y):
    screen.blit(platformImg[i], (x, y))


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, BLACK)
    screen.blit(score, (x, y))


def isCollsion(playerX, playerY, platformX, platformY):
    distance = math.sqrt((math.pow(playerX - platformX, 2) + math.pow(playerY - platformY, 2)))

    if distance < 50:
        return True
    else:
        return False

def save_score():
    f = open('score.txt', 'w')
    f.write(f'The score is {score_value}')

# Main Loop
running = True
while running:
    # Fill the screen
    screen.fill((W))
    # Show the background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

            if event.key == pygame.K_LEFT:
                playerX_change = -5

        if event.type == pygame.KEYUP:
            playerX_change = 0

    # Border Checking for the player
    if playerX < 0:
        playerX = 750

    if playerX > 750:
        playerX = 0

    if playerY > 530:
        playerY = 530

    if playerY < 10:
        playerY = 300
        score_value += 1
        platformX[i] = (random.randint(0, 690))
        platformY[i] = (random.randint(60, 500))

    # Collision wih platform and player
    for i in range(num_of_platforms):
        collision = isCollsion(playerX, playerY, platformX[i], platformY[i])
        if collision:
            playerY -= 200

        platform(platformX[i], platformY[i])

    # Show the game objects
    playerY += playerY_change
    playerX += playerX_change
    player(playerX, playerY)
    show_score(textX, textY)



    # Update the screen
    player(playerX, playerY)
    pygame.display.update()
    save_score()
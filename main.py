import pygame
import random
import math

pygame.init()
width = 800
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("icons/space-invaders.png")
pygame.display.set_icon(icon)
score=0
font=pygame.font.Font('freesansbold.ttf',32)


over=pygame.font.Font('freesansbold.ttf',64)
def game_over():
    game=font.render("Game Over",True,(255,255,255))
    screen.blit(game,(200,250))

textX=10
textY=10

def show_score(x,y):
    score_1=font.render("Score :"+str(score),True,(255,255,255))
    screen.blit(score_1,(x,y))

background = pygame.image.load("icons/bg.png")
bullet_img = pygame.image.load("icons/bullet.png")
# player profile
player_image = pygame.image.load("icons/space.png")
playerX = 370
playerY = 480
player_movement = 0


def player(x, y):
    screen.blit(player_image, (x, y))


bulletX = 0
bulletY = 480
bulletX_movement = 0
bulletY_movement = 5
bullet_state = "ready"


def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 22, y + 10))


# enemy profile

enemy_image = []
enemyX = []
enemyY = []
enemyX_movement = []
enemyY_movement = []

number_of_enemies=6
for i in range(number_of_enemies):
    enemy_image.append(pygame.image.load("icons/spaceship.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_movement.append(3)
    enemyY_movement.append(40)


def enemy(x, y,i):
    screen.blit(enemy_image[i], (x, y))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(((enemyX - bulletX) ** 2) + ((bulletY - enemyY) ** 2))

    if distance < 27:
        return True
    else:
        return False


is_running = True

while is_running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, -100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_movement = -5
            if event.key == pygame.K_RIGHT:
                player_movement = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet(playerX, bulletY)
                    bulletX = playerX
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_movement = 0
    playerX += player_movement

    for i in range(number_of_enemies):
        if enemyY[i]>440:
            for j in range(number_of_enemies):
                enemyY[i]=2000
            game_over()
            break
        enemyX[i] += enemyX_movement[i]
        if enemyX[i] <= 0:
            enemyX_movement[i] = 3
            enemyY[i] += enemyY_movement[i]
        elif enemyX[i] >= 736:
            enemyX_movement[i] = -3
            enemyY[i] += enemyY_movement[i]
        collision=is_collision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bullet_state="ready"
            bulletY=480
            score+=1
            print(score)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i],i)
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    if bullet_state == "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_movement
    if bulletY <= 0:
        bullet_state = "ready"
        bulletY = 480
    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()

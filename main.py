#
#
# Space Invaders
# Author: Muhammad Ali
# Date: 23 November 2024
#
# Information:
# Description:
# Space Invaders is a classic arcade game that was released in 1978 and designed by Tomohiro Nishikado. The game is a fixed shooter where players control a spaceship that must defend Earth from invading alien forces. The objective is to destroy waves of descending aliens with the spaceship's lasers while avoiding their counterattacks. As the game progresses, the alien formations speed up, creating an increasingly challenging and intense experience.

# Features:
# - Player-controlled spaceship with left and right movement
# - Alien invaders moving in formation, descending toward the player
# - Shields providing temporary protection from enemy shots
# - Boss enemy appearances for added challenge

# Controls:
# - Left Arrow: Move spaceship left
# - Right Arrow: Move spaceship right
# - Spacebar: Fire bullets to eliminate enemies

# How to Play:
# 1. Defend Earth by eliminating waves of invading aliens.
# 2. Avoid enemy fire and collisions with the aliens.
# 3. Earn points for each defeated alien and try to achieve the highest score.
# 5. Survive as long as possible to become the ultimate Space Invaders

# some part of player shots and and some part of sheild code,  i took help converting into function


#necessary imports
from pygame import *
from random import *

#background song
mixer.init()
mixer.music.load('song.mp3')
mixer.music.play()

#shot sound
shot_sound = mixer.Sound('shot.mp3')


#animation for blitting two images
enemy_animation_frame = 0
enemy_animation_timer = time.get_ticks()




screen = display.set_mode((1150,850))   #making screen
background = image.load("background.png")   #importing background
background = transform.scale(background, (1150,850))

#variables for player corrdinates
w = 510/5
h = 540/5
x = 575-78.5
y = 725

#loading graphics required
intro = image.load("intro.png")
space_ship = image.load("space_ship.png")
space_ship = transform.scale(space_ship, (w,h))
bullet = image.load("bullet.png")
bullet = transform.scale(bullet, (5,20))
shield1 = image.load("shield.png")
shield1 = transform.scale(shield1, (128,96))
shield1Rect = shield1.get_rect().move(127,600)  #creating rectangle on the sheild
shield2 = image.load("shield.png")
shield2 = transform.scale(shield2, (128,96))
shield2Rect = shield2.get_rect().move(127*3,600)
shield3 = image.load("shield.png")
shield3 = transform.scale(shield3, (128,96))
shield3Rect = shield3.get_rect().move(127*5,600)
shield4 = image.load("shield.png")
shield4 = transform.scale(shield4, (128,96))
shield4Rect = shield4.get_rect().move(127*7,600)

enemy = image.load("enemy.png")
enemy = transform.scale(enemy, (37*1.5,25*1.5))
enemy2 = image.load("enemy2.png")
enemy2 = transform.scale(enemy2, (37*1.5,25*1.5))
enemy3 = image.load("enemy3.png")
enemy3 = transform.scale(enemy3, (96/2.5,96/2.5))
enemy1_type2 = image.load("enemy alt.png")
enemy1_type2 = transform.scale(enemy1_type2, (37*1.5,25*1.5))
enemy2_type2 = image.load("enemy2 alt.png")
enemy2_type2 = transform.scale(enemy2_type2, (37*1.5,25*1.5))
enemy3_type2 = image.load("enemy3 alt.png")
enemy3_type2 = transform.scale(enemy3_type2, (96/2.5,96/2.5))
boss_enemy = image.load("boss_enemy.png")
boss_enemy = transform.scale(boss_enemy, (191/2,85/2))

enemy_bullet = image.load("enemy_bullet.png")
enemy_bullet = transform.scale(enemy_bullet, (117/4,136/4))


#two pics that blitts while moving
pics = [enemy, enemy1_type2]
pics2 = [enemy2, enemy2_type2]
pics3 = [enemy3, enemy3_type2]

#text function, got it from online, helps write text more easily
def display_text(surface, text, pos, font, color):   #got the function online for displaying text on the next line
    collection = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    x,y = pos
    for lines in collection:
        for words in lines:
            word_surface = font.render(words, True, color)
            word_width , word_height = word_surface.get_size()
            if x + word_width >= 800:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x,y))
            x += word_width + space
        x = pos[0]
        y += word_height

#initializing score variable, to count scores
score = 0
font.init()
Font = font.SysFont("Visitor", 90)   #Setting the font for the title

#necessar lists to store shots and type of enemies
enemy_shots = []
shots = []
enemies1 = []   #storing enemies in different type of list cuz they count for different points
enemies2 = []
enemies3 = []

#draws rectangle on player
class Player(Rect):
    def __init__(self,x,y,img):
        super().__init__(x, y, w, h)
        self.img = img
playerRect= Player(x,y,space_ship)
#draws rectangle on enemies
class Enemy(Rect):
    def __init__(self,x,y,img):
        super().__init__(x, y, 37*1.5, 25*1.5)
        self.img = img

#using different class for the smaller enemy, to adjust with size and stuff
class Enemy3(Rect):
    def __init__(self,x,y,img):
        super().__init__(x, y, 96/2.5, 96/2.5)
        self.img = img

#rectangle for boos
class Boss(Rect):
    def __init__(self,x,y,img):
        super().__init__(x, y, 191/2,85/2)
        self.img = img

#appending images in the list
for x_coordinates in range(150,851,70):
    enemies1.append(Enemy(x_coordinates,350,enemy))
    enemies1.append(Enemy(x_coordinates,300,enemy))
    enemies2.append(Enemy(x_coordinates,250,enemy2))
    enemies2.append(Enemy(x_coordinates,200,enemy2))
    enemies3.append(Enemy3(x_coordinates,150,enemy3))

def draw_enemies():
    global enemy_animation_frame, enemy_animation_timer

    #got animation thing where it blitts two images at the same time, got it from online
    # Update the animation frame based on the timer
    current_time = time.get_ticks()
    if current_time - enemy_animation_timer > 500:  # Adjust the duration as needed (500 milliseconds in this example)
        enemy_animation_timer = current_time
        enemy_animation_frame = 1 - enemy_animation_frame  # Switch between 0 and 1

    for en in enemies1:
        draw.rect(screen, (255, 0, 0), en)
        # Use the updated animation_frame to determine which image to display
        if en in enemies1:
            screen.blit(pics[enemy_animation_frame], en)
    for en in enemies2:
        draw.rect(screen, (255, 0, 0), en)
        if en in enemies2:
            screen.blit(pics2[enemy_animation_frame], en)
    for en in enemies3:
        if en in enemies3:
            screen.blit(pics3[enemy_animation_frame], en)


#horizaontal and vertical movement of enemies
move_X = 2
move_Y = 5
def moveEnemy():
    global move_X
    global move_Y
    hitWall = False
    for e in enemies1 + enemies2 + enemies3:
        e[0]+=move_X
        if e[0]<0 or e[0]>1050: #check it it hits the corner
            hitWall = True
    if hitWall:
        move_X = -(move_X)  #changes the value when hits the corner
    for e in enemies1 + enemies2 + enemies3:
        if hitWall:
            e[1] += move_Y
def bulletCollidngEnemy(s):
    #checks the collision of the enemy
    #took a little help to fix bugs in it
    global score
    collided = False
    for enemy in enemies1 + enemies2 + enemies3:
        if enemy.collidepoint(s):
            if enemy in enemies1:
                enemies1.remove(enemy)
                score+=10   #adds scores based on the type of enemy
            elif enemy in enemies2:
                enemies2.remove(enemy)
                score+=20
            elif enemy in enemies3:
                enemies3.remove(enemy)
                score+=40
            collided = True
            break
    return collided


def enemyShooting():
    #enemy shotting bullets
    for enemy in enemies1 + enemies2 + enemies3:
        if randint(1,1000) == 1:    #propability of enemy shooting
            enemy_shots.append([enemy[0],enemy[1]])

def detect_enemy_bullet_collision(shield, shieldrect, s, x, y):
    #detecs when enemy bullet hits the sheild
    if shieldrect.collidepoint(s):
        r, g, _, _ = shield.get_at((x, y))
        if r < 50 and g > 220:
            draw.rect(shield,(0,0,0),(x, y,randint(20,20),randint(20,20)))
            return True
def moveEnemyShots(shots):
    for shot in enemy_shots:
        for i in range(10):
            s = [int(shot[0]), int(shot[1])]
            shot[1]+=1  #moves the shot corridinate
            if detect_enemy_bullet_collision(shield1, shield1Rect, s, s[0]-127, s[1]-600) or detect_enemy_bullet_collision(shield2, shield2Rect, s, s[0]-(127*3), s[1]-600) or detect_enemy_bullet_collision(shield3, shield3Rect, s, s[0]-(127*5), s[1]-600) or detect_enemy_bullet_collision(shield4, shield4Rect, s, s[0]-(127*7), s[1]-600) :
                shots.remove(shot)
                break
def draw_shield(shield, dest):  #draws sheild
    screen.blit(shield, dest)
def draw_shields():
    screen.blit(background,(0,0))
    draw.line(screen,GREEN,(0,850),(1150,850),10)
    draw_shield(shield1, (127, 600))
    draw_shield(shield2, (127*3, 600))
    draw_shield(shield3, (127*5, 600))
    draw_shield(shield4, (127*7, 600))




def bulletCollidingPlayer(s):
    global running
    #exits the game when hit
    if playerRect.collidepoint(s):
        running = False
        return True
    return False


def enemyPlayerCollision(shots):
    for shot in enemy_shots:
        s = [int(shot[0]), int(shot[1])]
        #running the bullet colliding player
        if bulletCollidingPlayer(s):
            shots.remove(shot)
            break
def detect_collision(shield, shieldrect, s, x, y):
    if shieldrect.collidepoint(s):
        r, g, _, _ = shield.get_at((x, y))
        if r < 50 and g > 220:
            draw.rect(shield,(0,0,0),(x, y,randint(50,100),randint(50,100)))
            return True
def shield_collision(shots):
    #checks for sheild collison when player hits the shot
    for shot in shots:
            for i in range(20):
                shot[1] -= 1
                s = [int(shot[0]), int(shot[1])]
                if detect_collision(shield1, shield1Rect, s, s[0]-127, s[1]-600) or detect_collision(shield2, shield2Rect, s, s[0]-(127*3), s[1]-600) or detect_collision(shield3, shield3Rect, s, s[0]-(127*5), s[1]-600) or detect_collision(shield4, shield4Rect, s, s[0]-(127*7), s[1]-600):
                    shots.remove(shot)
                    break
                if bulletCollidngEnemy(s):
                    shots.remove(shot)
                    break

#restes level which allows to have infinite level, got it from online, mostly undestand it
def reset_level():
    global x, y, enemies1,enemies2,enemies3, boss_x, condition
    # Clear existing enemies
    enemies1 = []
    enemies2= []
    enemies3  = []
    # Reset boss
    boss_x = randint(100, 200)
    boss_x = -(boss_x)
    # Repopulate enemies for the new level
    for x_coordinates in range(150, 851, 70):
        enemies1.append(Enemy(x_coordinates, 350, enemy))
        enemies1.append(Enemy(x_coordinates, 300, enemy))
        enemies2.append(Enemy(x_coordinates, 250, enemy2))
        enemies2.append(Enemy(x_coordinates, 200, enemy2))
        enemies3.append(Enemy3(x_coordinates, 150, enemy3))

    condition = True  # Reset boss condition

#boss enemy stuff
condition = True
boss_x = randint(100,200)
boss_x = -(boss_x)
bossRect = Boss(boss_x,100,boss_enemy)

#commonly used colours
RED =   (255, 0, 0)    # ALL CAPS is used for constants
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
play_button = Rect(760, 495, 125, 50)

#got cooldown code form online, mostly understand it
cooldown = 60

#keeps menu true, until mouse isn't pressed
menu = True
while menu:
    for evt in event.get():
        if evt.type == QUIT:
            menu = False
            running = False
        elif evt.type == MOUSEBUTTONDOWN:
            if play_button.collidepoint(mouse.get_pos()):
                menu = False


    screen.blit(intro, (0, 0))
    draw.rect(screen,(155,244,244),play_button,1)

    display.flip()
running = True
while running:
    for evt in event.get():
        if evt.type == KEYDOWN:
            if evt.key == K_SPACE and cooldown == 0:
                shots.append([x+51, y]) #appends shot when spacebar is pressed
                shot_sound.play()

                cooldown = 30
        if evt.type == QUIT:
            running = False

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    # ----------------------------------
    #calling functions
    enemyShooting()
    enemyPlayerCollision(enemy_shots)
    moveEnemyShots(enemy_shots)
    moveEnemy() 
    shield_collision(shots)
    draw_shields()
    draw_enemies()

    #moving boss enemy and removing it when collides with bullet
    boss_x+=1
    bossRect = Boss(boss_x,100,boss_enemy)
    if condition == True:
        screen.blit(boss_enemy,(boss_x,100))

    #blitting player shots
    for shot in shots:
        screen.blit(bullet,(int(shot[0]),int(shot[1])))

        s = [int(shot[0]), int(shot[1])]
        if bossRect.collidepoint(s):
            condition= False
            score+=200
            shots.remove(shot)

    #blitting enemy shots
    for shot in enemy_shots:
        screen.blit(enemy_bullet,((shot[0]),(shot[1])))




    #moving player
    keys = key.get_pressed()
    screen.blit(space_ship,(x,y))
    for i in range(10):
        if keys[K_RIGHT] and x<1050:
            x += 1  #moves right when right key clicked
            screen.blit(space_ship,(x,y))
            playerRect= Player(x,y,space_ship)
        elif keys[K_LEFT] and x>0:
            x -= 1  #moves left when keys left clicked
            screen.blit(space_ship,(x,y))
            playerRect= Player(x,y,space_ship)

    cooldown = max(0, cooldown - 1)
    if len(enemies1) == 0 and len(enemies2) == 0 and len(enemies3) == 0:    #when no enemies are left, the game resets again
        reset_level()  # Reset the level
    display_text(screen, "SCORE " + str(score), (0, 0), Font, (255,255,255))    #displays the text
       #  ---------------------------------
    display.flip()

    time.wait(1)


quit()




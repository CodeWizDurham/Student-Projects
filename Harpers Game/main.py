import pygame
import random

pygame.init()
# This initalizes the pygame
screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Godzilla_game")
# This is the size of the screen
clock = pygame.time.Clock()
running = True

Godzilla_image = pygame.image.load("2 (1).png")
Godzilla_image = pygame.transform.scale(Godzilla_image, (238,131))

Antartica_image = pygame.image.load("mount fuji.png")
Antartica_image = pygame.transform.scale(Antartica_image, (1080, 800))

Enemy_1 = pygame.image.load("tank.png")
Enemy_1 = pygame.transform.scale(Enemy_1, (100, 50))
# This loads  all of the images that are in the current version of the game
Godzilla_x = 540
Godzilla_y = 600
Godzilla_pos = (Godzilla_x, Godzilla_y)
Tank_x = 50
Tank_y = 600
# These are the cordinates where the character spawns into the game 

Tanks = []

Godzilla_health = 3


placement = (Godzilla_x, Godzilla_y)
bk_x = 0
Enemy_placement = (Tank_x, Tank_y)
bk_x = 0

def move_character(placement):

    Godzilla_x, Godzilla_y = placement

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        Godzilla_y -= 5
    if keys[pygame.K_DOWN]:
        Godzilla_y += 5 

    return (Godzilla_x, Godzilla_y)  
# These keys allow my charcter to move around.
def spawn_tank():
    Tank_x = screen_width + random.randint(100, 500)
    Tank_y = random.randint(100, screen_height - 100)
    return (Tank_x, Tank_y)
def move_tanks():
    global Godzilla_health
    for i, tank in enumerate(Tanks):
        Tank_x, Tank_y = tank
        Tank_x -= 2 
        Tanks[i] = (Tank_x, Tank_y)   
        if abs(Tank_x - Godzilla_x) < 50 and abs(Tank_y - Godzilla_y):
            Godzilla_health -= 1
            Tanks.pop(i)
            if Godzilla_health <= 0:
                return True
    return False 

def draw_health_bar(Screen):
    font = pygame.font.Font(None, 36)
    text = font.render(f'Health:{Godzilla_health}', True, (255, 255, 255))
            
                        
def movingbackround(screen, x, image):
    screen.blit(image, (x,0))
    screen.blit(image, (x + 1080, 0))

        
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))    
    Godzilla_pos = move_character(Godzilla_pos)
    if random.randint(0, 100) < 2:
        Tanks.append(spawn_tank())

    Game_over = move_tanks()
    if Game_over:
        break

    
    bk_x -= 2

    if bk_x <= -1080: 
        bk_x = 0

    movingbackround(screen, bk_x, Antartica_image)
    # these lines have to do with the background
    # Drawing godzilla
    screen.blit(Godzilla_image, placement)
    for Tank in Tanks:
        screen.blit(Enemy_1, Enemy_placement)

    draw_health_bar(screen)
    pygame.display.update()   
    clock.tick(60)
    
font =pygame.font.Font(None, 72)
text = font.render('Game Over', True, (255, 0, 0))
text_rect = text.get_rect(center = (screen_width // 2, screen_height // 2))
screen.blit(text, text_rect)
pygame.display.update()
pygame.time.wait(2000)
    # This cloock tick is how many frames per second happen
pygame.quit
# This ends the pygame


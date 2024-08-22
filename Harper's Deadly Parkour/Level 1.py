import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Deadly Parkour")
clock = pygame.time.Clock()

# Load images
player_image = pygame.image.load("steve.png")
creeper_image = pygame.image.load("creep.png")
creeper_image = pygame.transform.scale(creeper_image, (100, 200))
player_image = pygame.transform.scale(player_image, (140, 132))
Cat_image = pygame.image.load("Cat.png")
Cat_image = pygame.transform.scale(Cat_image, (237, 142))

# Initial positions
creeper_x, creeper_y = 360, 550
player_x, player_y = 120, 550
Cat_x, Cat_y = 100, 550
# Game variables
creeper_speed = 10
player_speed = 10
player_health = 3
game_active = False

def draw_health_bar(health):
    bar_width = 200
    bar_height = 30
    fill_color = (255, 0, 0) if health > 0 else (128, 128, 128) # Red if health > 0, gray if not
    pygame.draw.rect(screen, (0, 0, 0), (50, 50, bar_width, bar_height), 2)  # Draw border
    pygame.draw.rect(screen, fill_color, (50, 50, bar_width * health / 3, bar_height))  # Draw fill

def display_message(message, color, size, position):
    font = pygame.font.Font(None, size)
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=position)
    screen.blit(text, text_rect)

def start_screen():
    global game_active
    screen.fill((0, 0, 0))
    display_message("Deadly Parkour", (255, 255, 255), 60, (screen_width / 2, screen_height / 2 - 30))
    display_message("Press ENTER to Start", (255, 255, 255), 30, (screen_width / 2, screen_height / 2 + 30))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                    game_active = True

def end_screen():
    global game_active
    screen.fill((0, 0, 0))
    if player_health <= 0:
        display_message("Game Over", (255, 0, 0), 60, (screen_width / 2, screen_height / 2 - 30))
    else:
        display_message("You Win!", (0, 255, 0), 60, (screen_width / 2, screen_height / 2 - 30))
    display_message("Press ESC to Quit", (255, 255, 255), 30, (screen_width / 2, screen_height / 2 + 30))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Main game loop
start_screen()

while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= player_speed
        Cat_y -= player_speed - 0.5
    if keys[pygame.K_DOWN]:
        player_y += player_speed
        Cat_y += player_speed - 0.5
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        Cat_x  -= player_speed - 0.5
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        Cat_x += player_speed - 0.5

    if keys[pygame.K_w]:
        creeper_y -= creeper_speed
    if keys[pygame.K_s]:
        creeper_y += creeper_speed
    if keys[pygame.K_a]:
        creeper_x -= creeper_speed
    if keys[pygame.K_d]:
        creeper_x += creeper_speed

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_image.get_width(), player_image.get_height())
    creeper_rect = pygame.Rect(creeper_x, creeper_y, creeper_image.get_width(), creeper_image.get_height())

    if player_rect.colliderect(creeper_rect):
        player_health -= 1
        creeper_x, creeper_y = 360, 550  # Reset creeper position
        if player_health <= 0:
            game_active = False

    # Drawing
    screen.fill((0, 0, 0)) 
    screen.blit(player_image, (player_x, player_y))
    screen.blit(creeper_image, (creeper_x, creeper_y))
    screen.blit(Cat_image,(Cat_x, Cat_y))
    draw_health_bar(player_health)
    pygame.display.update()
    clock.tick(60)

end_screen()
import pygame , sys
from pygame.locals import *
import random , time
pygame.init()
FPS= 60
FramePerSecond = pygame.time.Clock()
#DEFINING COLOURS______________________________________________________
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)     
#constants______________________________________________________________
SCREEN_WIDTH = 400
SCREEN_HEIGHT =600
SPEED =2
SCORE =0
#Setting up font________________________________________________________
font = pygame.font.SysFont("Verdana", 60)
small_font = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

DISPLAY = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAY.fill(WHITE)
pygame.display.set_caption("EB512")
#Enemy class_____________________________________________________________
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemycar.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)

    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE +=1
            self.rect.top = 0 #??
            self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)  
    def draw(self, surface):
        surface.blit(self.image, self.rect)
#player class______________________________________________________________
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("playercar.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressedkeys = pygame.key.get_pressed()

        if self.rect.left > 40:   
            if pressedkeys [K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH - 40:   
            if pressedkeys [K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = Player()
E1 = Enemy()

#creating sprite groups_______________________________________
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)

Inc_speed = pygame.USEREVENT +1
pygame.time.set_timer(Inc_speed,100)

while True:
    for event in pygame.event.get():
        if event.type == Inc_speed:
            SPEED +=0.1

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    DISPLAY.fill(WHITE)
    score = small_font.render(str(SCORE), True, BLACK)
    final_score = small_font.render("your score:" + str(SCORE), True, BLACK)
    DISPLAY.blit(score,(10,10))
    for entity in all_sprites:
        entity.draw(DISPLAY)
        entity.move()
        
    if pygame.sprite.spritecollideany(P1,enemies):
        DISPLAY.fill(RED)
        DISPLAY.blit(game_over,(30,250))
        DISPLAY.blit(final_score,(120,320))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()    
    pygame.display.update()
    FramePerSecond.tick(FPS)







# import lib. 
import pygame, sys, time

# import variables / functions
from settings import screen_width, screen_height
from text_import import game_name

# import classes
from level import Level

class Game():
    
    def __init__(self):
        # call the method to create the level
        self.create_level()
    
    def create_level(self):
        # create the level with the class Level
        self.level = Level(display_surface)
        self.status = 'level'
    
    def run(self, dt):
        # call the run method on level (IMPORTANT)
        self.level.run(dt)

# Pygame setup
pygame.init()
display_surface = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game()

# window setup
pygame.display.set_caption(game_name)
# pygame_icon = pygame.image.load(game_icon)
# pygame.display.set_icon(pygame_icon)

while True:
    # to get a user input
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        
        # to quite the game
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]: 
            pygame.quit()
            sys.exit()
    
    # overwrite the old level layer (IMPORTANT)
    display_surface.fill('black')
    
    # for the performance (FPS)
    dt = clock.tick() / 1000
    
    # run the game
    game.run(dt)
    pygame.display.update()
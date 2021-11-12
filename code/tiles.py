import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        # self.image = pygame.Surface((size,size))
        # self.image.fill('#ccd1d6')
        image = pygame.image.load('graphics/tiles/cloud.png').convert_alpha()
        self.image = pygame.transform.scale(image,(64,64))
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self,x_shift):
        self.rect.x += x_shift
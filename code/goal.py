import pygame

class Goal(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        image = pygame.image.load('graphics/goal/tresure_chest.png').convert_alpha()
        self.image = image
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self,x_shift):
        self.rect.x += x_shift
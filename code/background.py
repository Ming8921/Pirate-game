import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        image1 = pygame.image.load('graphics/background/Sky_background.jpg').convert_alpha()
        image2 = pygame.transform.scale(image1, (3000,900)) 
        self.image = image2
        self.rect = self.image.get_rect(topleft = pos)

    def update(self,x_shift):
        self.rect.x += x_shift

import pygame

class FakeWall(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        image = pygame.image.load('graphics/tiles/cloud.png').convert_alpha()
        self.image = pygame.transform.scale(image,(64,64)) #thay đổi kích thước hình ảnh 
        self.rect = self.image.get_rect(topleft = pos) #Khởi tạo hình chữ nhật bao phủ bề mặt của hình ảnh

    def update(self,x_shift):
        self.rect.x += x_shift 

import pygame, sys

from pygame.constants import QUIT
from settings import *
from level import Level

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height)) #setup chiều dài, chiều rộng cho màn hình giao diện

# icon,header,font
pygame.display.set_caption("Prirate") #set tên cho chương trình
icon = pygame.image.load("graphics/hat.png") #set hình ảnh cho icon chương trình
pygame.display.set_icon(icon)
font = pygame.font.Font('font/Pixeltype.ttf', 50) #set font chữ cho title

# Background song
bg_song = pygame.mixer.Sound('audio/bg_song.wav') #set âm thanh 
bg_song.set_volume(0.5) 
bg_song.play(loops = -1)

clock = pygame.time.Clock() #Thiết lập Fps cho chương trình
level = Level(level_map,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if level.game_active != 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    level = Level(level_map,screen)
                    level.game_active = 0

    if level.game_active == 0:
        screen.fill('black')
        level.run()
    elif level.game_active == 1:
        screen.fill('#e5fec8')
        image = pygame.transform.scale(icon,(128,64))
        screen.blit(image,(530,350))
        message = font.render('PRESS SPACE TO PLAY GAME',True,'#52c1f4')
        screen.blit(message,(400,500))
    elif level.game_active == -1:
        screen.fill('#e5fec8')
        image = pygame.transform.scale(icon,(128,64))
        screen.blit(image,(530,350))
        message1 = font.render('GAME OVER',True,'#52c1f4')
        screen.blit(message1,(515,440))
        message2 = font.render('PRESS SPACE TO PLAY GAME',True,'#52c1f4')
        screen.blit(message2,(400,500))
    elif level.game_active == 2:
        screen.fill('#e5fec8')
        image = pygame.transform.scale(icon,(128,64))
        screen.blit(image,(530,350))
        message1 = font.render('YOU HAVE WIN THE GAME',True,'#52c1f4')
        screen.blit(message1,(430,440))
        message2 = font.render('PRESS SPACE TO PLAY GAME',True,'#52c1f4')
        screen.blit(message2,(400,500))

    pygame.display.update()
    clock.tick(60)
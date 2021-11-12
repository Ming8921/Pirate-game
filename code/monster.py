import pygame
import random
from support import import_folder

GRAVITY =1
TILE_SIZE = 40
class Monster(pygame.sprite.Sprite):
    def __init__(self,pos,speed,z):
        self.z=z
        self.alive=True 
        self.direction=1
        self.speed=speed
        self.jump=False
        self.vel_y=0
        self.action = 0
        self.move_counter=0
        self.idling=False
        self.idling_counter=0
        self.in_air = False

        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['run'][self.frame_index]
        self.rect=self.image.get_rect(topleft = pos)
        self.monster_status = 'run'
        self.facing_left = True

    def import_character_assets(self):
        monster_path = 'graphics/enemy/'
        self.animations = {'run':[]}

        for animation in self.animations.keys():
            full_path = monster_path + animation #Lấy hình ảnh của monster
            self.animations[animation] = import_folder(full_path) #Truyền giá trị cho key trong dictionary

    def animate(self):
        animation = self.animations[self.monster_status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        image = animation[int(self.frame_index)]
        if self.facing_left: #Khi monster đi đến giới hạn phía bên trái
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False) #Cho monster đi theo hướng ngược lại
            self.image = flipped_image

    def update(self,x_shift):
        self.rect.x += x_shift

    def move(self, moving_left, moving_right):
        #reset movement variables
        dx = 0
        dy = 0

        #assign movement variables if moving left or right
        if moving_left:#Thiết lập các thông số cho monster di chuyển sang trái
            dx = -self.speed
            self.facing_left = True
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.facing_left = False
            self.flip = False
            self.direction = 1

        #jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -11 #nhảy lên cách mặt đất 11px
            self.jump = False
            self.in_air = True

        #apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        #check collision with floor 
        if self.rect.bottom + dy > self.z:
            dy = self.z - self.rect.bottom
            self.in_air = False

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def update_action(self, new_action):
        #check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            #update the animation settings
            # self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def ai(self):
        if self.idling == False and random.randint(1, 200) == 1:
            self.update_action(0)
            self.idling = True
            self.idling_counter = 50
        if self.idling == False:
            if self.direction == 1: #Thiết lập hướng di chuyển
                ai_moving_right=True
                self.jump = True
            else:
                ai_moving_right =False
                self.jump = True
            ai_moving_left = not ai_moving_right
            self.move(ai_moving_left,ai_moving_right)
            self.update_action(1)
            self.move_counter+=1
            if self.move_counter>TILE_SIZE:
                self.direction*=-1
                self.move_counter*=-1
        else:
            self.idling_counter-=1
            if self.idling_counter <=0:
                self.idling =False

        self.animate()
            

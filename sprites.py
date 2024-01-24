'''
Title: sprites
Developers: Anish Roy and Eric Xia
Purpose: all sprites used in the game 
''' 

import pygame
from pygame import sprite
from pygame.constants import K_SPACE
pygame.init()

tutorial_font = pygame.font.SysFont('Ariel', 25)

class Tile(pygame.sprite.Sprite): #tile sprite 
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.image.load('Assets/crate.png').convert() #image 
        self.image = pygame.transform.scale(self.image,(size,size)) #scaled to fit screen
        self.rect = self.image.get_rect(topleft = pos) #rect for image

    def update(self, x_shift): #shifts object by the world shift
        self.rect.x += x_shift

'''class Teleport(pygame.sprite.Sprite): #same as tile 
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.image.load('Assets/teleport.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(size,size))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift''' 

class Teleport(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door1.png'))
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door2.png'))
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door3.png'))
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door4.png'))
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door5.png'))
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door6.png'))
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door7.png'))
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door8.png'))
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door9.png'))
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door10.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image,(size,size))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

'''class Goal(pygame.sprite.Sprite): #same as tile
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.image.load('Assets/flag.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(size,size))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift'''

class Goal(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door1.png'))
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door2.png'))
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door3.png'))
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door4.png'))
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door5.png'))
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door6.png'))
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door7.png'))
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door8.png'))
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door9.png'))
        self.sprites.append(pygame.image.load('Assets/DoorSprites/door10.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image,(size,size))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

class Jump_Text(pygame.sprite.Sprite): #same as tile but with text
    def __init__(self,pos):
        super().__init__()
        self.image = tutorial_font.render("Press Space to Jump", 1, 'black')
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift

class Move_Text(pygame.sprite.Sprite):#same as tile but with text
    def __init__(self,pos):
        super().__init__()
        self.image = tutorial_font.render("Press A and D to move", 1, 'black')
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift

class DJump_Text(pygame.sprite.Sprite):#same as tile but with text
    def __init__(self,pos):
        super().__init__()
        self.image = tutorial_font.render("Press space midair to double jump", 1, 'black')
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift

class Player(pygame.sprite.Sprite): #anything to do with the player
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('Assets/he_idle.png').convert_alpha() #image of player
        self.image = pygame.transform.scale(self.image,(size,size)) #scales to fit screen
        self.rect = self.image.get_rect(topleft = pos) #rect for player

        #player movement variables
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 3.8
        self.current_speed = 0
        self.acceleration = 0.2
        self.gravity = 0.8
        self.jump_speed = -16
        self.double_jump = 0

    def player_input(self):
        keys = pygame.key.get_pressed() #controls
        if keys[pygame.K_d]: #go right
            self.direction.x = 1
        elif keys[pygame.K_a]: #go left
            self.direction.x = -1
        else: #not moving horizontally 
            self.direction.x = 0
            self.speed = 3.8

    def apply_gravity(self): #gravity for player 
        self.direction.y += self.gravity #continously increases speed at which the player falls
        self.rect.y += self.direction.y

    def apply_acceleration(self): #acceleration for player
        self.speed += self.acceleration #continously adds speed to player as they move in one direction
        if self.speed > 15: #limit fot speed
            self.speed = 15
        if self.speed > 1:
            self.current_speed = self.speed #value for the current speed of player

    def update(self):  #run player input
        self.player_input() 



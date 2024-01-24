'''
Title: level
Developers: Anish Roy and Eric Xia
Purpose: sets up the level for the game 
'''

import pygame
from settings import DOOR_SIZE, HEIGHT, TILE_SIZE, WIDTH, PLAYER_SIZE
import settings
from sprites import DJump_Text, Jump_Text, Move_Text, Player, Teleport, Tile, Goal

class Level:
    def __init__(self, level_data, surface):
        #level setup 
        self.display_surface = surface #window
        self.level_data = level_data #level map in a list
        self.location = 0 #location in list of level map
        self.setup_level(level_data) #sets up level

        self.world_shift = 0 #shifts world with player movement
        

    def setup_level(self, layout):
        self.text = False #if these values are apart of the map they are set to true
        self.tp = False
        self.goal_flag = False
        layout = layout[self.location] #accesses section of level

        self.tiles = pygame.sprite.Group() # groups for each sprite
        self.goal = pygame.sprite.GroupSingle() 
        self.player = pygame.sprite.GroupSingle()
        self.jump_text = pygame.sprite.GroupSingle()
        self.move_text = pygame.sprite.GroupSingle()
        self.djump_text = pygame.sprite.GroupSingle()
        self.teleport = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout): #checks each row of the level map 
            for col_index, cell in enumerate(row): #checks each cell in the row
                x = col_index * TILE_SIZE #location
                y = row_index * TILE_SIZE

                if cell == 'X': #places tiles 
                    tile = Tile((x,y), TILE_SIZE)
                    self.tiles.add(tile)
                if cell == 'P': #places the player
                    player_sprite = Player((x,y), PLAYER_SIZE)
                    self.player.add(player_sprite)
                if cell == 'G': #places the goal 
                    goal = Goal((x-5,y-14),DOOR_SIZE)
                    self.goal.add(goal)
                    self.goal_flag = True
                #text placed in level
                if cell == 'J': 
                    jump_text = Jump_Text((x,y))
                    self.jump_text.add(jump_text)
                    self.text = True
                if cell == 'M':
                    move_text = Move_Text((x,y))
                    self.move_text.add(move_text)
                    self.text = True
                if cell == 'D':
                    djump_text = DJump_Text((x,y))
                    self.djump_text.add(djump_text)
                    self.text = True
                
                if cell == 'T': #tile that teleports player to the next section of the level
                    teleport = Teleport((x-5,y-14), DOOR_SIZE)
                    self.teleport.add(teleport)
                    self.tp = True


    def scroll_x(self): #level scrolling
        player = self.player.sprite #variables to make things shorter
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < WIDTH // 4 and direction_x < 0: #shifts level forward
            self.world_shift = 8 + 5
            player.speed = 0
            direction_x = 0
        elif player_x > WIDTH - (WIDTH // 4) and direction_x > 0: #shifts level backwards
            self.world_shift = -8 - 5
            player.speed = 0
            direction_x = 0
        else:
            self.world_shift = 0 #no shift

    def horizontal_col(self): #horizontal collision between player and tiles
        player = self.player.sprite
        player.apply_acceleration() #player acceleration 

        player.rect.x += player.direction.x * player.speed #moves player 

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect): #checks for collision in any of the tiles in the level
                if player.direction.x > 0: #collision with left side of tiles
                    if sprite.rect.left <= player.rect.right and sprite.rect.centerx >= player.rect.right:
                        player.rect.right = sprite.rect.left 
                        player.speed = 6
                elif player.direction.x < 0: #collision with right side of tiles
                    if sprite.rect.right >= player.rect.left and sprite.rect.centerx <= player.rect.left:
                        player.rect.left = sprite.rect.right 
                        player.speed = 6

    def vertical_col(self): #vertical collision 
        player = self.player.sprite
        player.apply_gravity() #gravity of player

        for sprite in self.tiles.sprites(): #checks for collision with tiles
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: #collision with top of tiles
                    if sprite.rect.top <= player.rect.bottom and sprite.rect.centery >= player.rect.bottom:
                        player.rect.bottom = sprite.rect.top
                        player.direction.y = 0
                        player.double_jump = 0 #resets double jump
                elif player.direction.y < 0: #collision with bottom of tiles
                    if sprite.rect.bottom >= player.rect.top and sprite.rect.centery <= player.rect.top:  
                        player.rect.top = sprite.rect.bottom
                        player.direction.y = 0

        if player.rect.top < 0: #ceiling for level
            player.rect.top = 0
            player.direction.y = 0

    def teleportation(self): #sends player to next section of level

        player = self.player.sprite
        teleport = self.teleport.sprite

        if teleport.rect.colliderect(player.rect): #check collision between objects
            self.location += 1 
            self.setup_level(self.level_data) #sets next section of level up


    def reset(self, timeIN): #resets the player if they die or restart 
        player = self.player.sprite
        if player.rect.centery > HEIGHT + 200: #checks if player is below screen and a bit
            self.location = 0 #sends player back to start of level
            self.setup_level(self.level_data) #sets level up
            time = 0 #resets time
            return time
        else:
            return timeIN

    def lvl_complete(self, running): #checks for level completion 
        player = self.player.sprite
        goal = self.goal.sprite

        if self.goal_flag: #checks for collision between objects only if there is a goal in the level
            if goal.rect.colliderect(player.rect):
                running = False 
            else:
                running = True

        return running 

    def run(self):

        #player
        self.player.update()
        self.scroll_x() #put this here to see if it fixed a problem 
        self.horizontal_col()
        self.vertical_col()   
        self.player.draw(self.display_surface)

        #level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        
        #goal
        if self.goal_flag: 
            self.goal.update(self.world_shift)
            self.goal.draw(self.display_surface)
        #text
        if self.text:
            self.jump_text.update(self.world_shift)
            self.jump_text.draw(self.display_surface)

            self.move_text.update(self.world_shift)
            self.move_text.draw(self.display_surface)

            self.djump_text.update(self.world_shift)
            self.djump_text.draw(self.display_surface)
        #teleport
        if self.tp:
            self.teleportation()
            self.teleport.update(self.world_shift)
            self.teleport.draw(self.display_surface)

            
        
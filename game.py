'''
Title: game
Developers: Anish Roy and Eric Xia
Purpose: runs level for the game 
''' 

import pygame
from sys import exit

from pygame.event import post
from settings import *
from level import Level

pygame.init()

WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #window
pygame.display.set_caption('game')

BLACK = (0,0,0) #colours
 
FPS = 60

clock = pygame.time.Clock()

SKY = pygame.image.load('Assets/bgSky.png').convert() #background
SKY = pygame.transform.scale(SKY,(WIDTH,HEIGHT))

cont_button = pygame.Rect(WIDTH//2 - 200, HEIGHT//4 - 50, 400, 100)  #buttons for pause menu
exit_button = pygame.Rect(WIDTH//2 - 200, HEIGHT*(3/4) - 50, 400, 100)
retry_button = pygame.Rect(WIDTH//2 - 200, HEIGHT*(2/4) - 50, 400, 100)

time = 0     #timer for levels
timer_text = str(time)
time_down = pygame.USEREVENT + 1
pygame.time.set_timer(time_down, 1000)
timer_font = pygame.font.SysFont('Ariel', 30)

'''bgMusic = pygame.mixer.Sound('Assets/Counterattack.ogg')
bgMusic.set_volume(0.1)
bgMusic.play(loops = -1)''' 


def draw_window(level, lvl_incomplete, speed): 
    
    WIN.blit(SKY,(0,0)) #background

    if lvl_incomplete: #runs only when the player has not completed the level
        level.run() #draws level + player

        draw_text(f'TIME: {timer_text}', timer_font, BLACK, WIN, 45, 20) #draws timer
        draw_text(f'VEL: {speed}', timer_font, BLACK, WIN, 45, 40) #draws current player speed

    else: #level complete screen
        draw_text("Level Complete", timer_font, BLACK, WIN, WIDTH//2, HEIGHT//2)  
        draw_text(f'Final Time: {timer_text} seconds', timer_font, BLACK, WIN, WIDTH//2, HEIGHT//2 + 30) #time to beat level
        draw_text('Press Space to Continue.', timer_font, BLACK, WIN, WIDTH//2, HEIGHT//2 + 60 )

    pygame.display.update()

def draw_pause_menu(): #window for pause menu
    WIN.blit(SKY,(0,0)) #background 

    pygame.draw.rect(WIN, BLACK, cont_button) #continue button
    draw_text('Continue', timer_font, 'white', WIN, cont_button.centerx, cont_button.centery) 

    pygame.draw.rect(WIN, BLACK, exit_button) #exit button
    draw_text('Exit', timer_font, 'white', WIN, exit_button.centerx, exit_button.centery) 

    pygame.draw.rect(WIN, BLACK, retry_button) #retry button
    draw_text('Retry', timer_font, 'white', WIN, retry_button.centerx, retry_button.centery) 

    pygame.display.update()


def draw_text(text, font, color, surface, x, y): #it does what it says
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def pause_menu(game, player): #pause menu 
    menu = True

    while menu:
        clock.tick(FPS) #fps

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #exit game
                menu = False
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN: 
                if cont_button.collidepoint(event.pos): #button to go back to level
                    game = True
                    return game
                if exit_button.collidepoint(event.pos): #goes back to the level menu
                    game = False
                    return game
                if retry_button.collidepoint(event.pos): #retry the level
                    player.rect.centery = HEIGHT + 300 #puts player in location that activates level reset function
                    game = True 
                    return game

        draw_pause_menu()


def main(level_map, lvl_number):
    level = Level(level_map,WIN) #takes in the level map given and initializes level
    game = True
    level.setup_level(level_map) #creates level

    global time #timer stuff
    global timer_text 
    time = 0
    timer_text = str(time)

    highscore_check = True #only checks if player beat the highscore of the level once 

    lvl_incomplete = True   #while player is playing the level

    while game:

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #exit program
                game = False
                pygame.quit()
                exit()

            if lvl_incomplete:  #while user hasn't completed level

                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_SPACE or event.key == pygame.K_w: #jump button
                        player = level.player.sprite #seperate from other controls because other controls check
                        if player.direction.y ==  0 or player.double_jump < 2: #what buttons are pressed every frame
                            player.direction.y = player.jump_speed #while this checks what buttons are let go
                            player.double_jump += 1 #important for double jump
                        
                    if event.key == pygame.K_ESCAPE: #pause menu
                        player = level.player.sprite #takes in game if player exits the level
                        game = pause_menu(game, player) #takes in player if player restarts level
                
                if event.type == time_down: #counts up the time 
                    time += 1                   
                    timer_text = str(time)

            else: 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: #exits level in level complete screen
                        game = False

        if lvl_incomplete: #runs if player has not complete level
            time = level.reset(time) #sets time back to 300 if player dies
            timer_text = str(time)
            
            #checks if player has completed level. starts timer when level completed
            lvl_incomplete = level.lvl_complete(lvl_incomplete) 

            player = level.player.sprite
            speed = str(round(abs(player.current_speed * player.direction.x), 3)) #current speed of player

        else: 
            while highscore_check: #checks to see if player beat highscore
                with open('highscore.txt','r+') as highscore:
                    highscore.seek(0)
                    scoreLst = []
                    for line in highscore: #puts all values in a list
                        line = line.replace('\n','')
                        score = int(line)
                        scoreLst.append(score)

                    if scoreLst[lvl_number] > time: #if player beat highscore
                        scoreLst[lvl_number] = time #chnages highscore to player time 
                        for item in range(len(scoreLst)): #converts list into string values with \n
                            text = str(scoreLst[item]) + '\n'
                            scoreLst[item] = text
                            
                        highscore.seek(0) #beginning of file
                        highscore.truncate(0) #removes everythinf in file
                        highscore.writelines(scoreLst) #writes new list to file
                        highscore_check = False #exit loop and is only done once
                    else:
                        highscore_check = False #if player doesn't beat highscore

            
        draw_window(level, lvl_incomplete, speed) #draws window 
        clock.tick(FPS) #fps


if __name__ == "__main__": 
    main()
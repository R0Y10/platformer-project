'''
Title: menu
Developers: Anish Roy and Eric Xia
Purpose: menu for game 
'''

import pygame #importing stuff
import game
from sys import exit
from settings import *
pygame.init()

WIN = pygame.display.set_mode((WIDTH,HEIGHT))        #window 
pygame.display.set_caption('Generic Platformer Game')

BLACK = (0,0,0) #colours

SKY = pygame.image.load('Assets/bgSky.png').convert() #background image
SKY = pygame.transform.scale(SKY,(WIDTH,HEIGHT))

title_font = pygame.font.SysFont('Ariel', 75) #fonts

FPS = 60 

play_button = pygame.Rect(WIDTH//2 - 200, HEIGHT//2 - 50, 400, 100)  #buttons for menus 
tutorial_lvl_button = pygame.Rect(50, 300, 500, 50)   
level_one_button = pygame.Rect(600, 300, 500, 50)   

clock = pygame.time.Clock() #clock

def draw_main_window():   #draws main menu of game
    WIN.blit(SKY,(0,0)) #background

    draw_text('Game', title_font, BLACK, WIN, WIDTH//2, 100)    #title of game
    pygame.draw.rect(WIN, BLACK, play_button) #play button
    draw_text('Play', title_font, 'white', WIN, play_button.centerx, play_button.centery) 

    pygame.display.update()

def draw_LM_window():  #draws level menu of game
    WIN.blit(SKY,(0,0)) #background 

    draw_text('Game', title_font, BLACK, WIN, WIDTH//2, 100) #title
    #level buttons
    pygame.draw.rect(WIN, BLACK, tutorial_lvl_button) 
    draw_text('Tutorial', title_font, 'white', WIN, tutorial_lvl_button.centerx, tutorial_lvl_button.centery)
    pygame.draw.rect(WIN, BLACK, level_one_button)
    draw_text('Level One', title_font, 'white', WIN, level_one_button.centerx, level_one_button.centery)

    with open('highscore.txt', 'r') as highscore:  #gets highscore for each level
        highscore.seek(0)
        hiLst = []
        for line in highscore:
            line = line.replace('\n','')
            hiLst.append(line)
    #draws highscores 
    draw_text(f'Highscore: {hiLst[0]}', title_font, BLACK, WIN, tutorial_lvl_button.centerx, tutorial_lvl_button.centery +100)
    draw_text(f'Highscore: {hiLst[1]}', title_font, BLACK, WIN, level_one_button.centerx, level_one_button.centery + 100)      

    pygame.display.update()

def draw_text(text, font, color, surface, x, y):  #function to make drawing text on screen easier
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def main_menu():  #main menu function
    menu = True

    while menu:
        clock.tick(FPS) #fps 

        for event in pygame.event.get():

            if event.type == pygame.QUIT:  #exit game
                menu = False
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  #goes to level menu when buttom is pressed
                if play_button.collidepoint(event.pos):
                    level_menu()

        draw_main_window() #draws menu

    main_menu()

def level_menu():
    running = True

    while running:
        clock.tick(FPS) #fps

        for event in pygame.event.get():

            if event.type == pygame.QUIT:  #exit game
                running = False
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN: #go back to main menu
                if event.key == pygame.K_ESCAPE:
                    running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN: #check if button is pressed and which level
                if tutorial_lvl_button.collidepoint(event.pos): #each level inputs a different map layout to the game
                    game.main(tutorial, 0) #level map and level number are inputted to game
                if level_one_button.collidepoint(event.pos):
                    game.main(level_one, 1)

        draw_LM_window() #draw level menu


if __name__ == "__main__": 
    main_menu()
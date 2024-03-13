'''
Title: settings
Developers: Anish Roy and Eric Xia
Purpose: contains level maps and size of stuff
'''

level_map = [
    '                            ',
    '                            ',
    '                            ',
    ' XX    XXX            XX    ',
    ' XX P                     G ',
    ' XXXX         XX         XX ',
    ' XXXX       XX              ',
    ' XX    X  XXXX    XX  XX    ',
    '       X  XXXX    XX  XXX   ',
    '    XXXX  XXXXXX  XX  XXXX  ',
    'XXXXXXXX  XXXXXX  XX  XXXX  ',]
test_map = [
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '  P              T      G   ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',]

lvl_one_sect_one = [
    '                       X                        X      X      X            X   X   X         XX',
    '                                                X      X      X            X   X   X         XX',
    '                       X               XXX      X      X      X            X       X         XX',
    '                       X                        X      X      X            X   X   X         XX',
    ' P                     X                        X      X      X                X   X         XX',
    ' XXXXXXXXXXXX          X       XXX             XX      X      X     X          X   X         XX', 
    '                       XX                       XX     X      X      X     X   X   X         XX',
    '                                                      XX       X           X   X             XX',
    '                                                       XX      X X         X   X              T',
    '                 XXX                                           X           X   X   X       XXXX',
    '                                                             X             X   X   X       X   ',]

lvl_one_sect_two = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX        X                X           G  ',
    'XXXXXXXXX                                               X     XX X         XXXXXX X        X  X  ',
    'XXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX XX     X X              X X        X     ',
    'X     X     X                    X X     X  X  X  XX  X X      X XXXXXXXXXX     X X        X     ',
    'X     X     X                    X X        X         X X      X X              X X        X     ',
    'X P        XX                    X    X  X  X     XX    X      X X         XXXXXX XXXXXX   X     ',
    'X X         X                    X    X  X  X  X        XX     X X              X X        X     ',
    'X     X     X                    X    X  X     X  XX  X X      X XXXXXXXXXX     X X        X     ',
    'XXXXXXX     XXXXXXXXXXXXXXXXXXXXXX XXXXXXXXXXXXXXXXXXXXXX XXXXXX X              X X        X     ',
    'XXXXXXXXXX                       X                        X            XXXXXX   X          X     ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX          XXXXXXX     X     ']


tutorial_map = [
    '                                                 X',
    '                                                 X',
    '                                              G  X',
    '                                  XXXXXXXXXXXXXXXX',
    '                                  XXXXXXXXXXXXXXXX',
    '                                  XXXXXXXXXXXXXXXX',
    '                            D     XXXXXXXXXXXXXXXX',
    '                                  XXXXXXXXXXXXXXXX',
    '    M                  J   XXXXXXXXXXXXXXXXXXXXXXX',
    '  P                        XXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',]


testing = [test_map, level_map]

level_one = [lvl_one_sect_one, lvl_one_sect_two]

tutorial = [tutorial_map]

TILE_SIZE = 50
PLAYER_SIZE = 47
DOOR_SIZE = 40
WIDTH = 1152
HEIGHT = 11*TILE_SIZE   #11x50

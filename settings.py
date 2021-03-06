#Color
BLACK = (0,0,0)
RED = (255,0,0)
GRAY = (51,51,51)

#Size
SCREEN_SIZE = (800,500)
CARD_SIZE = (120,180)
TB_SIZE = (100,150)
CHIP_SIZE = (50,50)
FIN_BTN_SIZE = (200,50)
YES_NO_BTN_SIZE = (100,50)

PLAY_CHIPS = {'ORANGE_CHIP' : 1, 
               'GREEN_CHIP' : 5, 
               'RED_CHIP' : 50, 
               'BLUE_CHIP' : 100 , 
               'BLACK_CHIP' : 500,
                }

#Position
BETTING_POS = [
        (100,100), #player
        (210,100), #player_pair
        (320,100), #tie
        (430,100), #banker_pair
        (540,100), #banker
]

CHIP_LOCATIONS = [
        [25,400], #orange
        [125,400], #green
        [225,400], #red
        [325,400], #blue
        [425,400], #black
]

FIN_BTN_LOCATION = [550,425]
YES_BTN_LOCATION = [100,425]
NO_BTN_LOCATION = [200,425]


BLIND_LOCATION = [SCREEN_SIZE[0]+100, 50]
ONE_MORE_CARD_BLIND_LOCATION = [900, 240]

CARD_LOCATIONS = [
        [50,50],
        [380,50],
        [180,50],
        [510,50],
#One more card (horizontal)
        [50,240],
        [380,240],
]

# Text Location 
P_SCORE_LOCATION = (50, 240)
B_SCORE_LOCATION = (380, 240)

P_VALUE_LOCATION = (50, 265)
B_VALUE_LOCATION = (380, 265)

USER_PROFILE_LOCATION = [
        (560, 330), #bet money
        (560, 360), #current money 
        (560, 390), #grade
]

RECORD_LOCATION = [
        [200,100], #it has to move, that's why the type is list, not tuple
]

FPS = 60

CARD_SPEED = 300
VX_TIME = 10 #속력 * vx_time(배수)
VY_TIME = 10 #속력 * vx_time(배수)

#Current_bet 
CURRENT_BET = {
                "player" : 0,
                "player_pair" :0,
                "tie" : 0,
                "banker_pair" : 0,
                "banker" : 0
                }

BET_OPTIONS = ["player" , "player_pair", "tie", "banker_pair", "banker"]

#Cards Deck
DECK = {
        'Ace' : 1, 
        2:2, 3:3, 
        4:4, 5:5, 
        6:6, 7:7, 
        8:8, 9:9, 
        10:0, 'J':0, 
        'Q':0, 'K':0
        }

#Record 
CURRENT_RECORD = {
        'winner' : None,
        'tie' : False,
        'player_pair' : False,
        'banker_pair' : False
}


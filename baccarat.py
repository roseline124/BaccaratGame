# coding = utf-8
import sys
import pygame as pg
import pickle, os 
from settings import *
from tables import *
from sprites import *
from pygame.locals import *

#Baccarat.py
class Baccarat : 
    def __init__(self) :
        pg.init()
        pg.display.set_caption('Baccarat')
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
    
    def new(self) : #init sprites
        self.all_sprites = pg.sprite.Group() #sprites.group
        self.background = Background(self, 'image/background_image.png', (0,0))
        
        #gamers
        self.user = User()
        self.player = Player('player')
        self.banker = Player('banker')

        #chips 
        self.orange_chip = Chips(self, ORANGE_CHIP)
        self.green_chip = Chips(self, GREEN_CHIP)
        self.red_chip = Chips(self, RED_CHIP)
        self.blue_chip = Chips(self, BLUE_CHIP)
        self.black_chip = Chips(self, BLACK_CHIP)

        self.orange_chip.new('image/orange_chip.png', CARD_LOCATION)
        self.green_chip.new('image/green_chip.png', CARD_LOCATION2)
        self.red_chip.new('image/red_chip.png', CARD_LOCATION3)
        self.blue_chip.new('image/blue_chip.png', CARD_LOCATION4)
        self.black_chip.new('image/black_chip.png', CARD_LOCATION5)
        
        #tables
        self.card_table = Card_Table()
        self.score_table = Score_Table()
        self.record_table = Record_table()

        #betting tables init
        self.tb_player = Bet_Table(self,'image/tb_player.png', TB_P_POS)
        self.tb_player_pair = Bet_Table(self,'image/tb_player_pair.png', TB_P_PAIR_POS)
        self.tb_tie = Bet_Table(self,'image/tb_tie.png', TB_TIE_POS)
        self.tb_banker_pair = Bet_Table(self,'image/tb_banker_pair.png', TB_B_PAIR_POS)
        self.tb_banker = Bet_Table(self,'image/tb_banker.png', TB_B_POS)
        
        #betting table
        self.betting_table = {self.tb_player : "player"
                            , self.tb_player_pair : "player_pair"
                            , self.tb_tie : "tie"
                            , self.tb_banker_pair : "banker_pair"
                            , self.tb_banker : "banker"}
        
        #operating elements 
        self.finish_btn = Button(self, 'image/finish_btn.png')

    def run(self) :
        self.playing = True 
        self.drag = False
        
        while self.playing : 

            pg.time.delay(100) #pause the program for the amount of time
            self.events()
            self.update()
            self.draw()

    
    def quit(self) :
        pg.quit()
        sys.exit()
    
    def events(self) :
        
        for event in pg.event.get() :
            
            #Quit
            if event.type == pg.QUIT :
                self.quit()
            elif event.type == pg.KEYDOWN :
                if event.key == pg.K_ESCAPE :
                    self.quit()
                    
            #Mouse #betting
            elif event.type == pg.MOUSEBUTTONDOWN :
                if event.button == 1 :
                    self.drag=True
                    self.offset_o = self.orange_chip.mouse_down(event.pos)                    
                    self.offset_g = self.green_chip.mouse_down(event.pos)  
                    self.offset_r = self.red_chip.mouse_down(event.pos)  
                    self.offset_sky = self.blue_chip.mouse_down(event.pos)  
                    self.offset_black = self.black_chip.mouse_down(event.pos) 

                    #deal
                    print("dealing")
                    self.answer = self.finish_btn.clicked(event.pos, self.card_table.deal, (self.player))
                    if self.answer == 1 : 
                        self.card_table.deal(self.banker)
                        self.card_table.deal(self.player)
                        self.card_table.deal(self.banker)

                        #count
                        print("counting")
                        self.score_table.count(self.player)
                        self.score_table.count(self.banker)
                        
                        #check values
                        print("checking")
                        self.score_table.check_value(self.player)
                        self.score_table.check_value(self.player)

                        #one more draw?
                        if (self.player.value == 'nothing') & (self.banker.value == 'nothing') :
                            print("-------------------------------------------\n",
                                "One more card!")

                            self.card_table.one_more(self.player, self.banker)

                        #score again
                        self.score_table.count(self.player)
                        self.score_table.count(self.banker)

                        #record
                        self.record_table.record(self.player, self.banker)

                        #pay 
                        self.cash_table = Cash_Table()
                        self.cash_table.pay(self.user)

                        print("-------------------------------------------\n"+
                        "your score : %d\n" %self.user.get_score(self.user.earnings, self.user.loss) +
                        "your money : %d\n" %USER_PROFILE['SEED_MONEY'] +
                        "your grade : %s\n" %self.user.rank(),)

            elif event.type == pg.MOUSEBUTTONUP : 
                if event.button == 1 :
                    self.drag = False 

                    #Collide (Betting)
                    self.orange_chip.bet(self.betting_table)
                    self.green_chip.bet(self.betting_table)                            
                    self.red_chip.bet(self.betting_table)                            
                    self.blue_chip.bet(self.betting_table)                            
                    self.black_chip.bet(self.betting_table)                            
                 
            elif event.type == pg.MOUSEMOTION : 
                if self.drag : 
                    self.orange_chip.mouse_drag(event.pos, self.offset_o)                                        
                    self.green_chip.mouse_drag(event.pos, self.offset_g)                                        
                    self.red_chip.mouse_drag(event.pos, self.offset_r)                                        
                    self.blue_chip.mouse_drag(event.pos, self.offset_sky)                                        
                    self.black_chip.mouse_drag(event.pos, self.offset_black)                                        
        
    def update(self) :
        self.all_sprites.update()
        pg.display.flip() #draw 
        
    def draw(self) :
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)

        
if __name__ == "__main__":
    baccarat = Baccarat()

    baccarat.new()
    baccarat.run()
import pygame as pg
import time
import sys
from .board import Board
from .dice import Dice
from .player import Player
pg.init()

class GameManager:
    PLAYER_CHANGED=pg.USEREVENT+3
    

    def __init__(self):
        self.win_width=1200
        self.win_height=900
        self.win=pg.display.set_mode((self.win_width,self.win_height))
        self.clock = pg.time.Clock()
        
        #Creating board and dice
        self.board=Board(self.win)
        self.dice=Dice(self.win)
        

        #Creating players
        self.createPlayers()

        #Player list
        self.createPlayerList()

        self.draw_player_name= True
        self.players_in_game=3
        self.player_ranks=[]
        self.game_over=False
        self.restart = False

        self.gameLoop()

       
       

    def createPlayers(self):
        self.player_red=Player(self.win,"red",self.board.board_matrix,"Player 1")
        self.player_yellow=Player(self.win,"yellow",self.board.board_matrix,"Player 2")
        self.player_blue=Player(self.win,"blue",self.board.board_matrix,"Player 3")
        self.player_green=Player(self.win,"green",self.board.board_matrix,"Player 4")

        self.board.updatePlayerTurnText(self.player_red)

    def createPlayerList(self):
        self.player_list=[self.player_red,self.player_yellow,self.player_blue,self.player_green]
        self.current_player=0

    def gameLoop(self):
        while True :
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type==pg.MOUSEBUTTONDOWN and self.dice.rect.collidepoint(pg.mouse.get_pos()) and self.dice.dice_roll :
                    if not self.game_over:
                        self.dice.startAnim()
                        self.dice.dice_roll=False
                    
                   
                if event.type==Dice.DICE_ANIM_STOP_EVENT :
                    self.player_list[self.current_player].createMovePath(self.dice.total_value)
                    self.dice.total_value=0
                    print("event hit")
                    self.board.show_roll_text=False


                if event.type==Player.PLAYER_MOVEMENT_STOPPED:
                    self.dice.dice_roll=True
                    self.draw_player_name= False
                    self.changeCurrentPlayer()
                    
                if event.type == GameManager.PLAYER_CHANGED:
                    self.board.updatePlayerTurnText(self.player_list[self.current_player])

                if event.type==self.dice.ROLL_AGAIN_SIGNAL:
                    self.board.show_roll_text=True
                
                if event.type==Player.PLAYER_WON:
                    self.players_in_game-=1
                    self.player_ranks.append(self.player_list[self.current_player].name)

                    self.board.playerWon(self.player_ranks)

                    self.player_list.pop(self.current_player)
                    self.current_player-=1
                    if len(self.player_list)<2:
                        self.game_over=True
                        self.board.is_game_over = True
                        
                        

                if event.type == pg.MOUSEBUTTONDOWN and self.board.restart_button_rect.collidepoint( pg.mouse.get_pos()) and self.game_over:
                        
                        
                    self.restart_game()
                    self.restart = True
               
                    

                
                
           
                     
            #Update Everything
            self.updateEverything()

            #Draw Everything
            self.drawEverything()

            pg.display.update()
            self.clock.tick(60) 

    def changeCurrentPlayer(self):
        self.current_player+=1
        
        if self.current_player>self.players_in_game:
            self.current_player=0
        
        pg.event.post(pg.event.Event(GameManager.PLAYER_CHANGED))



    
    def updateEverything(self):
        self.dice.update()
        self.player_red.update()
        self.player_yellow.update()
        self.player_blue.update()
        self.player_green.update()
    
    def drawEverything(self):
        self.board.drawBoard()
        self.dice.drawDice()
        self.player_red.drawPlayer()
        self.player_yellow.drawPlayer()
        self.player_blue.drawPlayer()
        self.player_green.drawPlayer()
       
        

    
    def restart_game(self):
        
        
        self.draw_player_name= True
        self.players_in_game=3
        self.game_over=False
        self.board.is_game_over = False
        self.player_ranks.clear()
        self.player_list.clear()
        self.createPlayerList()
        self.board.updatePlayerTurnText(self.player_list[self.current_player])
        for player in self.player_list:
            player.setInitialValuesback()
        self.dice.setInitialValues()
        self.drawEverything()

        

            

       
   
            
        

        
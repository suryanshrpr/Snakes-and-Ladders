import pygame as pg


class Board:
    

    def __init__(self,win_ref) -> None:
        self.win=win_ref
        
        self.board_img=pg.image.load("assets/board1.png").convert_alpha()
        self.board_img_rect=self.board_img.get_rect(center=(500,450))
        
        self.board_matrix=[[0,0,0,0,0,0,0,0,0,0,0,0],
                           [0,1,"l1e",1,"s1s",1,"s2s",1,1,"l2e",1,0],
                           [0,1,1,1,1,1,1,1,"s3s",1,1,0],
                           [0,"l1s",1,"s1e",1,"l4e",1,1,1,1,"l2s",0],
                           [0,1,"s4s",1,1,1,1,"l3e",1,1,1,0],
                           [0,1,1,1,1,"s2e",1,1,1,1,1,0],
                           [0,1,"l5e",1,1,1,1,1,"s6s",1,"l3s",0],
                           [0,1,1,"l6e","s5s",1,1,1,1,"s7s",1,0],
                           [0,"l5s",1,1,"s3e",1,"s6e",1,"l4s",1,"l8e",0],
                           [0,1,1,"s4e",1,1,1,"l7e",1,1,1,0],
                           [0,"l6s",1,1,"l7s","s5e",1,1,"l8s",1,"s7e",0],
                           [0,0,0,0,0,0,0,0,0,0,0,0],]
    
        self.font = pg.font.Font("assets/arial.ttf",30)  
        self.player_name=""     
        self.player_name_rect=None
        self.player_color=""
        self.player_color_rect=None
        self.show_roll_text=False
        self.roll_again_text= self.font.render("Roll Again" , True , (255,255,255))
        self.roll_again_text_rect = self.roll_again_text.get_rect(center= (1050,300))

        self.game_over_text= self.font.render("Game Over" , True , (255,255,255))
        self.game_over_text_rect = self.game_over_text.get_rect(center= (1050,800))
        
        self.restart_button= self.font.render("Restart" , True , (255,255,255))
        self.restart_button_rect = self.restart_button.get_rect(center= (1050,850))

        self.player_ranks_display= self.font.render("PLayer Ranks" , True , (255,255,255))
        self.player_ranks_display_rect = self.player_ranks_display.get_rect(center= (1050,570))
        
        self.is_game_over = False
       

        

    def drawBoard(self):
        self.win.fill((30,30,30))
        self.win.blit(self.board_img,self.board_img_rect)
        self.win.blit(self.player_name,self.player_name_rect)
        self.win.blit(self.player_color, self.player_color_rect)
        
        if self.show_roll_text:
            self.win.blit(self.roll_again_text,self.roll_again_text_rect)

        if self.is_game_over :
            self.win.blit(self.player_ranks_display,self.player_ranks_display_rect)
            self.win.blit(self.game_over_text, self.game_over_text_rect)
            self.win.blit(self.restart_button, self.restart_button_rect)
            self.win.blit(self.player_won1, self.player_won_rect1)
            self.win.blit(self.player_won2, self.player_won_rect2)
            self.win.blit(self.player_won3, self.player_won_rect3)

      


    def playerWon(self,list_ref):
        
                
        
        for i in list_ref:
            

            if  len(list_ref) ==1 and  list_ref[0]  :
                self.player_won1= self.font.render(f"{i}" , True , (255,255,255))
                self.player_won_rect1 = self.player_won1.get_rect(center= (1050,590))
                
            if len(list_ref) ==2 and list_ref[1]:
                self.player_won2= self.font.render(f"{i}" , True , (255,255,255))
                self.player_won_rect2 = self.player_won2.get_rect(center= (1050,630))
                
            if len(list_ref) == 3 and list_ref[2] :
                self.player_won3= self.font.render(f"{i}" , True , (255,255,255))
                self.player_won_rect3 = self.player_won3.get_rect(center= (1050,670))
                
            

        
        



        


    def updatePlayerTurnText(self,player_obj_ref):

        
        self.player_name= self.font.render(f"{player_obj_ref.name}'s Turn" , True , (255,255,255))
        self.player_name_rect = self.player_name.get_rect(center= (1050,100))

        
        
        self.player_color= pg.image.load(f"assets/player_{player_obj_ref.color}.png").convert_alpha()
        
        if player_obj_ref.color =="blue":
            self.player_color_rect = self.player_color.get_rect(center= (1041,200))
        elif player_obj_ref.color =="red":
            self.player_color_rect = self.player_color.get_rect(center= (1072,200))
        elif player_obj_ref.color =="yellow":
            self.player_color_rect = self.player_color.get_rect(center= (1063,200))
        elif player_obj_ref.color =="green":
            self.player_color_rect = self.player_color.get_rect(center= (1028,200))

       
        
    

     
from typing import Any
import pygame as pg

class Player(pg.sprite.Sprite):
    PLAYER_MOVEMENT_STOPPED=pg.USEREVENT+2
    PLAYER_WON=pg.USEREVENT+5
    
    def __init__(self,win_ref,color,board_matrix_ref,name) -> None:
        super(Player, self).__init__()

        

        self.win=win_ref
        self.name=name
        self.color=color
        self.board_matrix=board_matrix_ref
        self.top_offset = 50
        self.left_offset = 100
        self.block_size = 80
        self.image=pg.image.load(f"assets/player_{self.color}.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.top=9*self.block_size+self.top_offset
        self.rect.left=0*self.block_size+20
        self.move_dir=1
        self.current_index=[10,0]
        self.move_path=[]
        self.start_moving=False
        self.anim_frame=0
        self.player_reached_final=False

        


    # def intitialPos(self):



    def setInitialValuesback(self):
        self.rect.top=9*self.block_size+self.top_offset
        self.rect.left=0*self.block_size+20
        self.move_dir=1
        self.current_index=[10,0]
        self.start_moving=False
        self.player_reached_final=False
        

        

    def drawPlayer(self):
        self.win.blit(self.image,self.rect)

    
    def createMovePath(self,dice_value):
        for i in range(0,dice_value):


            if self.move_dir==1:
                if self.board_matrix[self.current_index[0]][self.current_index[1]+1]==0:
                    self.current_index[0]=self.current_index[0]-1
                    self.move_dir*=-1
                    print("Moving up")

                else:
                    self.current_index[1]=self.current_index[1]+1
                    print("Moving right")
        
        
            else:
                if self.board_matrix[self.current_index[0]][self.current_index[1]-1]==0:
                    self.current_index[0]=self.current_index[0]-1
                    self.move_dir*=-1
                    print("Moving up")
                else:
                    self.current_index[1]=self.current_index[1]-1
                    print("Moving left")
        
            
                


            print("curr index:",self.current_index)
            

            self.move_path.append([self.current_index[0],self.current_index[-1]])

            if self.current_index==[1,1]:
                self.player_reached_final=True
                break
            

        transporter_value=self.board_matrix[self.current_index[0]][self.current_index[1]]
        to_transport=False
        
        
        


        if type(transporter_value)==str:
            print("trans value:",transporter_value)
            if transporter_value[0]=='l' and transporter_value[-1]=='s':
                destination='l'+transporter_value[1]+'e'
                to_transport=True
            elif transporter_value[0]=='s' and transporter_value[-1]=='s':
                destination='s'+transporter_value[1]+'e'
                to_transport=True
            if to_transport:
                self.current_index=self.findDestinationIndices(self.board_matrix,destination)
                self.move_path.append([self.current_index[0],self.current_index[-1]])
                if (self.current_index[0]-1)%2==0:
                    self.move_dir=-1
                else:
                    self.move_dir=1

            

        self.start_moving=True
        print("Move path:",self.move_path)
    
    def findDestinationIndices(self,matrix, destination):
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                if value == destination:
                    return [i,j]
                

    
    def update(self) -> None:  
        if self.start_moving:
            if self.anim_frame>20:
                if len(self.move_path)>0:
                    self.rect.top=((self.move_path[0][0]-1)*self.block_size)+self.top_offset
                    self.rect.left=((self.move_path[0][1]-1)*self.block_size)+self.left_offset
                    self.move_path.pop(0)
                    print("top-left:",self.rect.top,self.rect.left)
                else:
                    self.start_moving=False
                    if self.player_reached_final:
                        pg.event.post(pg.event.Event(Player.PLAYER_WON))
                    pg.event.post(pg.event.Event(Player.PLAYER_MOVEMENT_STOPPED))
                self.anim_frame=0
            else:
                self.anim_frame+=1

    
        
            
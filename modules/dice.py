from typing import Any
import pygame as pg
from random import randint
class Dice(pg.sprite.Sprite):
    DICE_ANIM_STOP_EVENT=pg.USEREVENT+1
    ROLL_AGAIN_SIGNAL=pg.USEREVENT+4
    def __init__(self,win_ref) -> None:
        super(Dice, self).__init__()
        self.win=win_ref
        self.img_dice_list = [pg.image.load(f"assets/{i}.png").convert_alpha() for i in range(1,7)] 
        self.image=self.img_dice_list[0]
        self.rect=self.image.get_rect(center=(1050,450))

        self.dice_roll_images=[pg.image.load(f"assets/roll{i}.png").convert_alpha() for i in range(1,9)]

        self.start_anim=False
        self.anim_counter=0
        self.dice_value=1
        self.anim_speed=5
        self.anim_play_frame=1
        self.dice_roll=True
        self.total_value=0
        self.is_six = False
    
        # self.val=0
        
    def setInitialValues(self):
        self.start_anim=False
        self.dice_roll=True
        self.total_value=0
        self.is_six = False

    def drawDice(self):
        self.win.blit(self.image,self.rect)

    def startAnim(self):
        self.start_anim=True
        self.setRandomDiceValue()

    def setRandomDiceValue(self):
        # if self.val==0:
        #     self.dice_value=6
        # else:
        #     self.dice_value=randint(1,6)
        self.dice_value=randint(1,6)
        self.total_value+=self.dice_value
        


    def update(self):
        if self.start_anim:
            if self.anim_play_frame<self.anim_speed:
                self.anim_play_frame+=1
            else:
                self.image=self.dice_roll_images[self.anim_counter]
                self.anim_counter+=1
                self.anim_play_frame=1
            if self.anim_counter>7:
                self.anim_counter=0
                self.start_anim=False
                self.image=self.img_dice_list[self.dice_value-1]
                if self.dice_value!=6 or self.total_value==18:
                    if self.total_value==18:
                        self.total_value=0
                    pg.event.post(pg.event.Event(Dice.DICE_ANIM_STOP_EVENT))
                    self.dice_roll=False
                else:
                    self.dice_roll=True
                    # if self.total_value==12:
                    #     self.val=18
                if self.dice_value==6 and self.total_value!=18:
                    pg.event.post(pg.event.Event(Dice.ROLL_AGAIN_SIGNAL))
                     
                




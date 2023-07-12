import pygame
import sys
from assets import *
import time
import random
import _thread

# Start
pygame.init()

class Game:

    def __init__(self):

        self.screen = pygame.display.set_mode((819, 432))
        self.d_ball_addr = (428, 215)
        self.randd = (0,0)

        self.player = None
        self.last_p = 0

        self.f_speed = 2
        
        self.bg_addr = (0, 0)
        self.palyer_addr = (35, 188)
        self.palyer_addr2 = (768, 188)
        self.ball_addr = (428, 215)
        self.bg_pic = pygame.image.load(bg_path)
        self.palyer_pic = pygame.image.load(player_pic)
        self.ball_pic = pygame.image.load(ball_pic)
        self.ball_move = self.randd 


    


    def if_(self):

        # Ball 

        if self.ball_addr[0] > 38 and self.ball_addr[0] < 768 and self.ball_addr[1] <= 38:   
               
             self.ball_move = (self.ball_move[0] , -self.ball_move[1])
             
        elif self.ball_addr[0]  > 37 and self.ball_addr[0] < 768 and self.ball_addr[1] >= 389 :   
             
             self.ball_move = (self.ball_move[0] , -self.ball_move[1])

        elif self.ball_addr[1] > self.palyer_addr[1] and self.ball_addr[1] < self.palyer_addr[1]+58 and self.ball_addr[0] <= 44:
            
             self.ball_move = (-self.ball_move[0] , self.ball_move[1])

        elif self.ball_addr[1] > self.palyer_addr2[1] and self.ball_addr[1] < self.palyer_addr2[1]+58 and self.ball_addr[0] >= 766:
            
             self.ball_move = (-self.ball_move[0] , self.ball_move[1])

        # Mouse

        if self.mouse[1] <= 49:

            self.palyer_addr = (self.palyer_addr[0],40)
        
        elif self.mouse[1] >= 344:
             
             self.palyer_addr = (self.palyer_addr[0],330)

        if self.player == "L":
             
             self.palyer_addr = (self.palyer_addr[0],self.mouse[1]-14)

        elif self.player == "R":
             
             self.palyer_addr = (self.palyer_addr2[0],self.mouse[1]-14)
       

       

    def ball(self):
    
         self.ball_addr = (self.ball_addr[0]+self.ball_move[0] , self.ball_addr[1]+self.ball_move[1])

    def event(self):

        self.mouse = pygame.mouse.get_pos()

        time.sleep(0.01)

        self.if_()
        

        if pygame.mouse.get_focused() == False:
             
             self.palyer_addr = (self.palyer_addr[0] , 188)

       
             
        
        for eve in pygame.event.get():
            
            if eve.type == pygame.QUIT:

                pygame.quit()

                sys.exit()

    def images(self):

        self.screen.blit(self.bg_pic , self.bg_addr)

        self.screen.blit(self.palyer_pic , self.palyer_addr)

        self.screen.blit(self.ball_pic , self.ball_addr)

        self.screen.blit(self.palyer_pic , self.palyer_addr2)
        

    def main(self):

        pygame.display.update()

        self.event()
        
        self.ball()

        self.images()


        
    



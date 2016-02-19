import pygame,random,sys

pygame.init()

screen=pygame.display.set_mode((960,480),0,32)

YELLOW=(255,230,0)

COINSIZE=10
class Coins:
    def __init__(self):
        self.player={'rect':pygame.Rect(5,462,20,20)}
        self.coins=[]
        self.i=0

    def genCoins(self):
        while self.i<=750:
            self.coins.append(pygame.Rect(self.i+100,462,COINSIZE,COINSIZE))
            self.i+=150
        
        self.i=0
        while self.i<=400:
            self.coins.append(pygame.Rect(self.i+100,382,COINSIZE,COINSIZE))
            self.i+=100

        self.i=300
        while self.i<=900:
            self.coins.append(pygame.Rect(self.i+100,302,COINSIZE,COINSIZE))
            self.i+=300
        
        self.i=0
        while self.i<=600:
            self.coins.append(pygame.Rect(self.i+100,222,COINSIZE,COINSIZE))
            self.i+=200
        
        self.i=200
        while self.i<=800:
            self.coins.append(pygame.Rect(self.i+100,142,COINSIZE,COINSIZE))
            self.i+=200
        

        self.coins.append(pygame.Rect(400,62,COINSIZE,COINSIZE))

    def drawCoins(self):
        for i in range(len(self.coins)):
            pygame.draw.rect(screen,YELLOW,self.coins[i])

        pygame.display.update()

    
        



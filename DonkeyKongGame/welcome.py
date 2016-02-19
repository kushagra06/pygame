import pygame, time

pygame.init()

screen=pygame.display.set_mode((960,480),0,32)

#colors(R,G,B)
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)


#Displaying welcome screen
class Message:
    def __init__(self):
        self.basicFont=pygame.font.SysFont("Courier",20)
        self.basicFont1=pygame.font.SysFont("Courier",18)
        self.text=self.basicFont.render("Welcome to Donkey Kong with shapes!",True,(0,0,0))
        self.text_char=self.basicFont.render("Characters",True,(0,0,0))
        self.text1=self.basicFont1.render("Instructions",True,(0,0,0))
        self.text0=self.basicFont1.render("Press SPACEBAR to continue",True,(0,0,0))
        self.text2=self.basicFont1.render("Free the princess from the castle",True,(0,0,0))
        self.text3=self.basicFont1.render("And make sure you collect all coins (5 points each)",True,(0,0,0))
        self.text4=self.basicFont1.render("Also don't collide with fireballs",True,(0,0,0))
        self.text5=self.basicFont1.render("Run away from fireballs",True,(0,0,0))
        self.text6=self.basicFont1.render("Jump using SPACEBAR",True,(0,0,0))
        self.text_keys=self.basicFont1.render("Use w-s-a-d to move",True,(0,0,0))
        self.text_player=self.basicFont1.render("Player",True,(0,0,0))
        self.text_donkey=self.basicFont1.render("Donkey",True,(0,0,0))
        self.text_princess=self.basicFont1.render("Princess",True,(0,0,0))
        self.text_ball=self.basicFont1.render("Fire Ball",True,(0,0,0))
        self.text_coin=self.basicFont1.render("Coin",True,(0,0,0))

    #first screen
    def writeText(self):
        screen.fill((255,255,255))
        screen.blit(self.text,(250,240))
        pygame.display.update()


    #character screen
    def characters(self):
        screen.fill(WHITE)
        screen.blit(self.text_char,(400,50))
        pygame.draw.rect(screen,GREEN,[300,100,20,20])
        pygame.draw.rect(screen,RED,[300,150,20,20])
        pygame.draw.circle(screen,GREEN,(310,200),10,0)
        pygame.draw.rect(screen,RED,[305,230,10,10])
        pygame.draw.rect(screen,YELLOW,[305,260,10,10])
        screen.blit(self.text_player,(400,100))
        screen.blit(self.text_donkey,(400,150))
        screen.blit(self.text_princess,(400,190))
        screen.blit(self.text_ball,(400,225))
        screen.blit(self.text_coin,(400,255))
        screen.blit(self.text0,(300,450))
        pygame.display.update()

    
    #instruction screen
    def instructions(self):
        screen.fill((255,255,255))
        screen.blit(self.text1,(400,50))
        screen.blit(self.text2,(250,100))
        screen.blit(self.text3,(250,150))
        screen.blit(self.text4,(250,200))
        screen.blit(self.text5,(250,250))
        screen.blit(self.text6,(250,300))
        screen.blit(self.text0,(300,460))
        screen.blit(self.text_keys,(250,400))
        pygame.display.update()



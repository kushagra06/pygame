import pygame

pygame.init()

screen=pygame.display.set_mode((960,480),0,32)

class Board:
    def __init__(self):
        #colors(R,G,B)
        self.BLACK=(0,0,0)
        self.WHITE=(255,255,255)
        self.RED=(255,0,0)
        self.GREEN=(0,255,0)
        self.BLUE=(0,0,255)


    def printBoard(self):
        screen.fill(self.WHITE) #background color
        #platform lines
        pygame.draw.line(screen,self.BLACK,(0,0),(960,0),10) 
        pygame.draw.line(screen,self.BLACK,(0,0),(0,480),10)
        pygame.draw.line(screen,self.BLACK,(960,0),(960,480),10)
        pygame.draw.line(screen,self.BLACK,(0,480),(960,480),10)
        pygame.draw.line(screen,self.BLACK,(0,80),(500,80),10)
        pygame.draw.line(screen,self.BLACK,(200,160),(960,160),10)
        pygame.draw.line(screen,self.BLACK,(0,240),(700,240),10)
        pygame.draw.line(screen,self.BLACK,(300,320),(960,320),10)
        pygame.draw.line(screen,self.BLACK,(0,400),(600,400),10)
        
        #prison
        pygame.draw.line(screen,self.RED,(150,10),(150,35),10)
        pygame.draw.line(screen,self.RED,(150,35),(300,35),10)
        pygame.draw.line(screen,self.RED,(300,10),(300,35),10)
        
        pygame.draw.circle(screen,self.GREEN,(225,20),10,0) #princess
        
        #Stairs
        pygame.draw.line(screen,self.BLUE,(250,40),(250,75),10)
        pygame.draw.line(screen,self.BLUE,(400,85),(400,155),10)
        pygame.draw.line(screen,self.BLUE,(275,165),(275,235),10)
        pygame.draw.line(screen,self.BLUE,(600,245),(600,315),10)
        pygame.draw.line(screen,self.BLUE,(450,325),(450,395),10)
        pygame.draw.line(screen,self.BLUE,(550,405),(550,475),10)

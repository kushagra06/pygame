import pygame
import time
import sys
import welcome 
import coin
import mainDK

#initialize pygame
pygame.init()

#making the display surface
screen=pygame.display.set_mode((960,480),0,32) 

clock=pygame.time.Clock() #setting up the clock

pygame.display.set_caption('Donkey Kong With Shapes! :)')

FPS=20 #frames per second


class Person:
    #The Person superclass
    def __init__(self):
        self.x=0
        self.y=0
        self.x_change=0
        self.y_change=0
        self.__myfont=pygame.font.SysFont("Courier",30) #setting up font to display text
    
    def getPosition(self):  #polymorphism
        pos=[self.x,self.y]
        return pos




class Donkey(Person):
    def __init__(self):
        self.x_donkey=0
        self.y_donkey=62
        self.donkey_direction=1




class Fireball:
    #setting fireballs coordinates
    def __init__(self):
        self.b1_x=400
        self.b2_x=500
        self.b3_x=800
        self.b4_x=10
        self.b5_x=200
        self.b6_x=700
        self.b7_x=0
        self.__myfont=pygame.font.SysFont("Courier",30)
    
    #when player loses a life, either with colliding with fireball or with donkey
    def lose(self):
        p.life-=1
        text0=self.__myfont.render("You lose a life!",True,(0,0,0))
        text1=self.__myfont.render("GameOver!",True,(0,0,0))
        if 1<=p.life<=3:  
            screen.blit(text0,(350,200))
            pygame.display.update()
            time.sleep(1.5)

        #when game is over
        elif p.life==0:
            while True:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                screen.blit(text1,(400,200))
                pygame.display.update()
            p.x=5
            p.y=462





class Player(Person):
    def __init__(self,x=0,y=0,x_change=0,y_change=0,x_donkey=0,y_donkey=0,donkey_direction=1):
        self.x=20
        self.y=462
        self.x_change=0
        self.y_change=0
        self.life=3
        self.__myfont=pygame.font.SysFont("Courier",30)
        self.coins=0
        self.state=0      #for jump: state=0 => On the ground and state=1 => In air
        self.velocity=60  #for jump: velocity first decreases, becomes zero then decreases

    
    #when player wins!
    def finalScreen(self):
        text=self.myfont.render("Winner!",True,(0,0,0))
        screen.blit(text,(400,200))
        pygame.display.update()


    #display scores
    def displayScore(self):
        text2=self.__myfont.render("Lives",True,(0,0,0))
        text1=self.__myfont.render(str(self.life),True,(0,0,0))
        text0=self.__myfont.render("Score",True,(0,0,0))
        text=self.__myfont.render(str(self.coins),True,(0,0,0))
        screen.blit(text,(900,10))
        screen.blit(text0,(800,10))
        screen.blit(text1,(900,440))
        screen.blit(text2,(800,440))
        pygame.display.update()

    
    #Check whether the player collides with fireball or donkey
    def checkCollision(self,playerRect,donkeyRect,b1,b2,b3,b4,b5,b6,b7):
        if playerRect.colliderect(b1) or playerRect.colliderect(b2) or playerRect.colliderect(b3) or playerRect.colliderect(b4) or playerRect.colliderect(b5)  or playerRect.colliderect(b6) or playerRect.colliderect(b7) or playerRect.colliderect(donkeyRect):
            p.x=5
            p.y=462
            fb.lose()
    
    
    #collect coins, when they are encountered
    def collectCoins(self,playerRect):
        for i in c.coins[:]:
            if playerRect.colliderect(i):
                c.coins.remove(i)
                p.coins+=5






def main():    
        #game loop starts
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  #to quit the game
                    pygame.quit()
                    sys.exit()



                if event.type == pygame.KEYDOWN: #when any key is pressed
                    if event.key==pygame.K_q:
                        pygame.quit()
                        sys.exit()


                    #move left if 'a' is pressed
                    if event.key==pygame.K_a and (p.y==462 or p.y==382 or p.y==302 or p.y==222 or p.y==142 or p.y==62):
                        p.x_change=-10
                        if p.x<=320 and p.y==302:
                            p.y=382
                            p.y_change=0
                        elif p.x<=220 and p.y==142:
                            p.y=222
                            p.y_change=0
                        elif p.x>=580 and p.y==382:
                            p.y=462
                            p.y_change=0
                        elif p.x>=680 and p.y==222:
                            p.y=302
                            p.y_change=0
                        elif p.x>=480 and p.y==62:
                            p.y=142
                            p.y_change=0


                    #move right if 'd' is pressed
                    elif event.key==pygame.K_d and (p.y==462 or p.y==382 or p.y==302 or p.y==222 or p.y==142 or p.y==62):
                        p.x_change=10
                        if p.x>=580 and p.y==382:
                            p.y=462
                            p.y_change=0
                        elif p.x>=680 and p.y==222:
                            p.y=302
                            p.y_change=0
                        elif p.x>=480 and p.y==62:
                            p.y=142
                            p.y_change=0
                        elif p.x<=320 and p.y==302:
                            p.y=382
                            p.y_change=0
                        elif p.x<=220 and p.y==142:
                            p.y=222
                            p.y_change=0



                    #move up if 'w' is pressed
                    elif event.key==pygame.K_w:
                        if 540<=p.x<=560 and p.y==462:
                            p.y=382
                            p.y_change=0
                        elif 430<=p.x<=460 and p.y==382:
                            p.y=302
                            p.y_change=0
                        elif 590<=p.x<=610 and p.y==302:
                            p.y=222
                            p.y_change=0
                        elif 265<=p.x<=285 and p.y==222:
                            p.y=142
                            p.y_change=0
                        elif 390<=p.x<=410 and p.y==142:
                            p.y=62
                            p.y_change=0
                        elif 240<=p.x<=260 and p.y==62:
                            p.y=15
                            p.y_change=0


                    #move down if 's' is pressed
                    elif event.key==pygame.K_s:
                        if 540<=p.x<=560 and p.y==382:
                            p.y=462
                            p.y_change=0
                        elif 430<=p.x<=460 and p.y==302:
                            p.y=382
                            p.y_change=0
                        elif 590<=p.x<=610 and p.y==222:
                            p.y=302
                            p.y_change=0
                        elif 265<=p.x<=285 and p.y==142:
                            p.y=222
                            p.y_change=0
                        elif 390<=p.x<=410:
                            p.y=142
                            p.y_change=0
                    

                    #jump if 'space' is pressed
                    elif event.key==pygame.K_SPACE:
                        if p.state==0:
                            p.state=1
                            p.velocity=20
                    
                    #if nothing is pressed, don't change x and y
                    else:
                        p.x_change=0
                        p.y_change=0




                
                #if the pressed key is released
                if event.type==pygame.KEYUP:
                    
                    if event.key==pygame.K_w:
                        p.y_change=0
                    
                    if event.key==pygame.K_s:
                        p.y_change=0
                    
                    if event.key==pygame.K_SPACE:
                        p.x_change=0
                    
                    if event.key==pygame.K_a and (p.y==462 or p.y==382 or p.y==302 or p.y==222 or p.y==142 or p.y==62):
                        p.x_change=0
                        if p.x<=320 and p.y==302:
                            p.y=382
                            p.y_change=0
                        elif p.x<=220 and p.y==142:
                            p.y=222
                            p.y_change=0
                        elif p.x>=580 and p.y==382:
                            p.y=462
                            p.y_change=0
                        elif p.x>=680 and p.y==222:
                            p.y=302
                            p.y_change=0
                        elif p.x>=480 and p.y==62:
                            p.y=142
                            p.y_change=0

                    if event.key==pygame.K_d and (p.y==462 or p.y==382 or p.y==302 or p.y==222 or p.y==142 or p.y==62):
                        p.x_change=0
                        if p.x>=580 and p.y==382:
                            p.y=462
                            p.y_change=0
                        elif p.x>=680 and p.y==222:
                            p.y=302
                            p.y_change=0
                        elif p.x>=480 and p.y==62:
                            p.y=142
                            p.y_change=0
                        elif p.x<=320 and p.y==302:
                            p.y=382
                            p.y_change=0
                        elif p.x<=220 and p.y==142:
                            p.y=222
                            p.y_change=0


            

            #final position of player
            p.x=(p.x+p.x_change)%960
            p.y=(p.y+p.y_change)%960

            #During jump, if velocity is -15, then the player is on ground
            if p.velocity==-15:
                p.state=0
            
            #if the player is in air
            if p.state==1:
                p.velocity-=5
                p.y=(p.y-p.velocity)



            #moving the fireballs
            fb.b1_x=(fb.b1_x+3)%960
            fb.b2_x=(fb.b2_x+5)%960
            fb.b3_x=(fb.b3_x+1)%960
            fb.b4_x=(fb.b4_x+3)%960
            fb.b5_x=(fb.b5_x+2)%960
            fb.b6_x=(fb.b6_x+4)%960
            fb.b7_x=(fb.b7_x+2)%960


            #moving the donkey
            if d.x_donkey==480:
                d.donkey_direction=-1
            if d.x_donkey==0:
                d.donkey_direction=1
            if d.x_donkey>=0 and d.donkey_direction==1:
                d.x_donkey+=1
            if d.x_donkey>=0 and d.donkey_direction==-1:
                d.x_donkey-=1



            #print the main screen
            b=mainDK.Board()
            b.printBoard()
            
            
            #draw the coins
            c.drawCoins()
            
            #display the score
            p.displayScore()
            
            
            pos=[]
            pos=p.getPosition()#polymorphism
            
            
            #draw fireballs
            b2=pygame.draw.rect(screen,(255,0,0),[fb.b2_x,302,10,10])
            b1=pygame.draw.rect(screen,(255,0,0),[fb.b1_x,382,10,10])
            b3=pygame.draw.rect(screen,(255,0,0),[fb.b3_x,302,10,10])
            b4=pygame.draw.rect(screen,(255,0,0),[fb.b4_x,222,10,10])
            b5=pygame.draw.rect(screen,(255,0,0),[fb.b5_x,142,10,10])
            b6=pygame.draw.rect(screen,(255,0,0),[fb.b6_x,142,10,10])
            b7=pygame.draw.rect(screen,(255,0,0),[fb.b7_x,62,10,10])

            
            #draw player and donkey
            playerRect=pygame.draw.rect(screen,(0,255,0),[p.x,p.y,15,15])
            donkeyRect=pygame.draw.rect(screen,(255,0,0),[d.x_donkey,d.y_donkey,15,15])

            
            p.checkCollision(playerRect,donkeyRect,b1,b2,b3,b4,b5,b6,b7) 
            
            p.collectCoins(playerRect)

            
            #if the player reaches the princess
            if p.y<=15:
                p.finalScreen()
            
            
            
            pygame.display.update()
            clock.tick(FPS)



#display the welcome screen
w=welcome.Message()
w.writeText()
time.sleep(1.5)
w.characters()


#instances of donkey, fireball, player and coins
d=Donkey()
fb=Fireball()
p=Player()    
c=coin.Coins()
c.genCoins()



#printing instructions
loop=True
while loop:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                w.instructions()
                loop=False
                break



#calling the main function
while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if __name__ == "__main__":
                    main()




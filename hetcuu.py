import pygame
from logic import lgi,ansbot
import random
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Hết cứu by HiShiGaming")
font = pygame.font.SysFont('pixel_font.ttf', 70)
text_Player  = font.render('Player: ', True, (0,0,0))
text_Result  = font.render('Result Bot: ', True, (0, 0, 0))
text_rep     =font.render((lgi("","")), False,(255, 255, 0))

clock=pygame.time.Clock()

gigachad=pygame.transform.scale(pygame.image.load(r'img/gigachad.png'),(100,100))
Keo =pygame.image.load(r'img/Keo.png')
Bua =pygame.image.load(r'img/Bua.png')
Bao =pygame.image.load(r'img/Bao.png')
icon=pygame.image.load(r'img\johnny sins.png')
background=pygame.transform.scale(pygame.image.load(r'img\hetcuu.png'),(1000,600))
img_result_bot=gigachad

pygame.display.set_icon(icon)

Keo=pygame.transform.scale(Keo,(100,100))
Bua=pygame.transform.scale(Bua,(100,100))
Bao=pygame.transform.scale(Bao,(100,100))


button_0 = pygame.Rect(200, 100, 100, 100)
button_1 = pygame.Rect(500, 100, 100, 100)
button_2 = pygame.Rect(800, 100, 100, 100)

running = True
while running:
    
    for event in pygame.event.get():
        bot=random.randint(0,2)
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bot=random.randint(0,2)
            if button_0.collidepoint(event.pos):
                text_rep=font.render((lgi(0,bot)), False,(255, 255, 0))        
            if button_1.collidepoint(event.pos):
                text_rep=font.render((lgi(1,bot)), False,(255, 255, 0)) 
            if button_2.collidepoint(event.pos):
                text_rep=font.render((lgi(2,bot)), False,(255, 255, 0))
            img_result_bot=ansbot(bot)
    img_result_bot=pygame.transform.scale(img_result_bot,(100,100))            
        
    screen.blit(background,(0,0))
    screen.blit(text_Player, (0, 50))
    screen.blit(text_Result, (0, 250))
    screen.blit(text_rep, (200,400))
    screen.blit(Keo, (200, 100))
    screen.blit(Bua, (500, 100))
    screen.blit(Bao, (800, 100))
    
    screen.blit(img_result_bot,(300,250))
    pygame.display.update()
    clock.tick(60)

pygame.quit()

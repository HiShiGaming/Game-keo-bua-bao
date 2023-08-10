import random
import pygame
def check_pk(user,bot):
    #Quy định return: 0 là bot thắng 1 là User thắng 2 là Hòa
    if user == bot :
        return 2
    elif user == 0 and bot == 1:
        return 0
    elif user ==1 and bot == 0:
        return 1
    elif user == 2 and bot == 0:
        return 0
    elif user ==0 and bot == 2:
        return 1
    elif user == 1 and bot == 2:
        return 0
    elif user == 2 and bot ==1:
        return 1

def ansbot(bot):
    if bot=="":
        return None
    if bot== 0: 
        return pygame.image.load(r'img/Keo.png')
    elif bot == 1:
        return pygame.image.load(r'img/Bua.png')
    elif bot == 2:
        return pygame.image.load(r'img/Bao.png')
    
def lgi(user,bot):
    if user=="":
        return "Nothing"
    if check_pk(user,bot)==2:
        return "Draw"
    if check_pk(user,bot)==1:
        return "Win"
    if check_pk(user,bot)==0:
        return "Lose"


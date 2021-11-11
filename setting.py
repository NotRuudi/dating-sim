
import pygame
from pygame.locals import *
from Images import load_pic

#VERY IMPORTANT to import code as from [filename] import [function] 
# otherwise will import as module not class
#Spreading out imports to reduce loadtimes


pygame.init()

size = (700,500)
#Hypikakna suurus
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Riigikogu")

#Sprites
class Girl(pygame.sprite.Sprite):
    #a cute girl
    def __init__(self):

        pygame.sprite.Sprite.__init__(self) #initialize sprite
        self.image = pygame.Surface([300,200])
        self.image.fill((255,255,255,))
        self.image.set_colorkey((255,255,255))
        self.image = load_pic("kaja_free.png").convert_alpha()
        self.rect = self.image.get_rect()
        
#nupud
from tkinter import *
from tkinter import messagebox
from Button import Button
#tkinter needs to be imported first

def esimene_nupp():
    messagebox.showinfo("Kaja Kallas:",":)")

def teine_nupp():
    messagebox.showinfo("Kaja Kallas:",":(")


nupp1 = Button("Jah!",500,50,100,50,esimene_nupp)
nupp2 = Button("Ei..",500,150,100,50,teine_nupp)
#Arvamused

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))



bg = load_pic("riigikogu.jpg")
bg = bg.convert()
background.blit(bg,(0,0))
screen.blit(background,(0,0))
pygame.display.flip()


clock = pygame.time.Clock()

sprites = pygame.sprite.Group()
girl = Girl()
sprites.add(girl)
sprites.update()

screen.blit(background,(0,0))
sprites.draw(screen)

if pygame.font:
    font = pygame.font.Font(None,35)
    tekst = font.render("Kas sa panid 6la alla?",1,(255,255,255))
    position = tekst.get_rect(centerx = background.get_height()/3)
    screen.blit(tekst,position)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        nupp1.handle_event(event)
        nupp2.handle_event(event)

    nupp1.update()
    nupp2.update()


    nupp1.draw(screen)
    nupp2.draw(screen)

    pygame.display.update()


pygame.quit()
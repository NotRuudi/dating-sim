import abc
import pygame_gui
import pygame
from pygame.locals import *
from pygame_gui.elements import UITextBox, UIButton
from Images import load_pic


#VERY IMPORTANT to import code as from [filename] import [function] 
# otherwise will import as module not class
#Spreading out imports to reduce loadtimes


pygame.init()

size = (700,500)
#Hypikakna suurus
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dialoogi simulaator")


KEY_REPEAT_SETTING = (200,70)

#Paarisarvulised indeksid on nupp1 , paaritud nupp 2
Options1 = [":)","Hea!"]
Options2 = [":(","Halb"]
Conversation = ["Kas sa panid 6la alla?","Mida sa  minu valitsusest arvad?"]

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
from Button import Button

i = 0

def esimene_nupp():
    global i
    dialoog = Options1[i]
    pygame.draw.rect(screen, (0,0,0), (10,400,500,100))
    font = pygame.font.Font(None,35)
    tekst = font.render(dialoog,1,(255,255,255))
    position = (10,400)
    screen.blit(tekst,position)
    i += 1


def teine_nupp():
    global i
    dialoog = Options2[i]
    pygame.draw.rect(screen, (0,0,0), (10,400,500,100))
    font = pygame.font.Font(None,35)
    tekst = font.render(dialoog,1,(255,255,255))
    position = (10,400)
    screen.blit(tekst,position)
    i += 1



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

pygame.draw.rect(screen, (0,0,0), (10,400,500,100))

if pygame.font:
    convo = Conversation[i]
    font = pygame.font.Font(None,35)
    tekst = font.render(convo,1,(255,255,255))
    position = (10,400)
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

    pygame.display.update()

    nupp1.draw(screen)
    nupp2.draw(screen)

    pygame.display.update()


pygame.quit()
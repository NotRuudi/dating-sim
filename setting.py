import os, sys
import pygame_gui
import pygame
from pygame.locals import *
from pygame import mixer
from pygame_gui.elements import UITextBox, UIButton
from Images import load_pic


#VERY IMPORTANT to import code as from [filename] import [function] 
# otherwise will import as module not class
#Spreading out imports to reduce loadtimes


pygame.init()
mixer.init()
sound= os.path.join("Assets", "bgmusic.mp3")
pygame.mixer.music.load(sound)
pygame.mixer.music.play(-1)
size = (700,500)
#Hypikakna suurus
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dialoogi simulaator")


KEY_REPEAT_SETTING = (200,70)

#Paarisarvulised indeksid on nupp1 , paaritud nupp 2

Conversation = [
    "Kas sa said selle projekti valmis?"
    ]
Jaatus = [
    "Nii tore! Kas ma peaks puhkusele minema?",
    "Kas ma peaks soojale maale minema?",
    "Sa oled vist heas tujus täna?",
    "Kas sa tahad nalja kuulda?",
    "Kopp-Kopp",
    "Sellisele naljale ei vastata nii.",
    "Igastahes, head tööpäeva."
    ]
Eitus = [
    "Veider. Kas ma peaks tööst pausi tegema?",
    "Kas ma peaks soojale maale minema?",
    "Kas sa oled halvas tujus täna..",
    "Kas sa tahad nalja kuulda?",
    "Kopp-Kopp",
    "Sellisele naljale ei vastata nii.",
    "Ma jälgin, kuidas sa täna tööd teed."
    ]
#Sprites
class Girl(pygame.sprite.Sprite):
    #a cute girl
    def __init__(self):

        pygame.sprite.Sprite.__init__(self) #initialize sprite
        self.image = pygame.Surface([300,300])
        self.image.fill((255,255,255,))
        self.image.set_colorkey((255,255,255))
        self.image = load_pic("bisnesman.png").convert_alpha()
        self.rect = self.image.get_rect()
        


#nupud
from Button import Button

i = 0

def esimene_nupp():
    global i
    pygame.draw.rect(screen, (0,0,0), (10,400,600,300))
    pygame.display.update()
    convo = Jaatus[i]
    font = pygame.font.Font(None,35)
    tekst = font.render(convo,1,(255,255,255))
    position = (10,400)
    screen.blit(tekst,position)
    i += 1


def teine_nupp():
    global i
    pygame.draw.rect(screen, (0,0,0), (10,400,600,300))
    pygame.display.update()
    convo = Eitus[i]
    font = pygame.font.Font(None,35)
    tekst = font.render(convo,1,(255,255,255))
    position = (10,400)
    screen.blit(tekst,position)
    i += 1



nupp1 = Button("Jah",500,50,100,50,esimene_nupp)
nupp2 = Button("Ei",500,150,100,50,teine_nupp)


background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))


#Title screen
black=(0,0,0)
end_it=False
while (end_it==False):
    screen.fill(black)
    bg = load_pic("kontor.jpg")
    bg = bg.convert()
    background.blit(bg,(0,0))
    screen.blit(background,(0,0))

    myfont=pygame.font.SysFont("Britannic Bold", 40)
    pygame.draw.rect(screen, (0,0,0), (170,200,400,80))
    nlabel=myfont.render("Teretulemast kontorisse!", 1, (255,255,255))
    mlabel=myfont.render("-Dialoogi simulaator-", 1, (255,255,255))
    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN:
            end_it=True
        if event.type == pygame.QUIT:
            quit()
    screen.blit(nlabel,(200,200))
    screen.blit(mlabel,(225,250))
    pygame.display.flip()


background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))



bg = load_pic("kontor.jpg")
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

pygame.draw.rect(screen, (0,0,0), (10,370,600,400))

if pygame.font:
    nimi = "Ülemus: "
    convo = Conversation[i]
    font = pygame.font.Font(None,35)
    tekst2 = font.render(nimi,1,(255,255,255))
    tekst = font.render(convo,1,(255,255,255))
    position = (10,400)
    screen.blit(tekst2,(10,370))
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
import os,sys
import pygame
import pygame.freetype
from pygame.locals import *
from tkinter import *
from tkinter import messagebox

pygame.init()

size = (700,500)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("game")


def load_pic(a):
    #name = os.path.join("data",a)
    try:
        img = pygame.image.load(a)
    except pygame.error as message:
        print("Cannot load image: ", a)
        raise SystemExit(message)
        img = img.convert()
    return img

class Girl(pygame.sprite.Sprite):
    #a cute girl
    def __init__(self):

        pygame.sprite.Sprite.__init__(self) #initialize sprite
        self.image = pygame.Surface([300,200])
        self.image.fill((255,255,255,))
        self.image.set_colorkey((255,255,255))
        self.image = load_pic("kaja_free.png").convert_alpha()
        self.rect = self.image.get_rect()
        

class Button():
    def __init__(self,text,x=0,y=0,width=100,height=50,command = None):
        self.text = text
        self.command = command

        self.image_normal = pygame.Surface((width,height))
        self.image_normal.fill((255,182,193))

        self.image_hovered = pygame.Surface((width,height))
        self.image_hovered.fill((221,241,251))

        self.image = self.image_normal
        self.rect = self.image.get_rect()

        tyyp = pygame.font.Font(None,35)

        text_image = tyyp.render(text, True, (0,0,0))
        text_rect = text_image.get_rect(center = self.rect.center)

        self.image_normal.blit(text_image,text_rect)
        self.image_hovered.blit(text_image,text_rect)

        self.rect.topleft = (x,y)

        self.hovered = False

    def update(self):
        if self.hovered:
            self.image = self.image_hovered
        else:
            self.image = self.image_normal

    def draw(self, surface):

        surface.blit(self.image, self.rect)

    def handle_event(self, event):

        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                if self.command:
                    self.command()
    

def esimene_nupp():
    messagebox.showinfo("Kaja Kallas:",":)")

def teine_nupp():
    messagebox.showinfo("Kaja Kallas:",":(")


nupp1 = Button("Jah!",500,50,100,50,esimene_nupp)
nupp2 = Button("Ei..",500,150,100,50,teine_nupp)


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
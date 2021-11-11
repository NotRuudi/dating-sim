import os,sys
import pygame
import pygame.freetype
from pygame.locals import *
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
    text = font.render("Kas sa panid 6la alla?",1,(255,255,255))
    position = text.get_rect(centerx = background.get_height()/3)
    screen.blit(text,position)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
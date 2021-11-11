import pygame
import os, sys
#Adding an extra directory so all images can be pulled from 1 folder


#Erinevate piltide sisselaadimine
def load_pic(a):
    full_name = os.path.join("Assets", a)
    try:
        img = pygame.image.load(full_name)
    except pygame.error as message:
        print("Cannot load image: ", a)
        raise SystemExit(message)

    return img
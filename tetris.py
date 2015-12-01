######################################
#Tetris                              #
#Märt Konsap ja Daniel Kütt          #
#inf3                                #
#2015                                #
######################################

import pygame, random, sys
from pygame.locals import *


AKNAK6RGUS = 640
AKNALAIUS  = 480
KASTISUURUS= 25
LAUALAIUS  = 10
LAUAK6RGUS = 20
# lauasuurus on kastisuuruse järgi, ehk laius on 10*25 = 250 pikslit
TOP_BOT_ÄÄRIS = (AKNAK6RGUS - LAUAK6RGUS*KASTISUURUS)//2
VASAK_ÄÄRIS   = KASTISUURUS
PAREM_ÄÄRIS   = AKNALAIUS - (LAUALAIUS*KASTISUURUS + VASAK_ÄÄRIS)
############### 480 - (10*25 + 25) = 205
VALGE = (255,255,255)
HALL  = (185,185,185)
MUST  = (  0,  0,  0)


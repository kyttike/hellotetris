######################################
#Tetris                              #
#Märt Konsap ja Daniel Kütt          #
#inf3                                #
#2015                                #
######################################

import pygame, random, sys
from pygame.locals import *


<<<<<<< HEAD
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
=======
AKNAKÕRGUS = 800
AKNALAIUS  = 640
KASTISUURUS= 20


VALGE       = (255,255,255)
HALL        = (185,185,185)
MUST        = (  0,  0,  0)
TPUNANE     = (204,  0,  0)
PUNANE      = (255,  0,  0)
HPUNANE     = (255,102,102)
TROHELINE   = (  0,204,  0)
ROHELINE    = (  0,255,  0)
HROHELINE   = (102,255,102)
TORANZ      = (  0,  0,  0)
ORANZ       = (  0,  0,  0)
HORANZ      = (  0,  0,  0)
TSININE     = (  0,  0,  0)
SININE      = (  0,  0,  0)
HSININE     = (  0,  0,  0)
TKOLLANE    = (  0,  0,  0)
KOLLANE     = (  0,  0,  0)
HKOLLANE    = (  0,  0,  0)
TAKVA       = (  0,  0,  0)
AKVA        = (  0,  0,  0)
HAKVA       = (  0,  0,  0)
TLILLA      = (  0,  0,  0)
LILLA       = (  0,  0,  0)
HLILLA      = (  0,  0,  0)

>>>>>>> origin/master


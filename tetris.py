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
TYHI_RUUT = "."


#Värvide defineerimine
#Iga kasti joonistamiseks kasutame kolme värvi
#ning kast on ümbritsetud musta joonega.

VALGE       = (255,255,255)
HALL        = (185,185,185)
MUST        = (  0,  0,  0)
TPUNANE     = (204,  0,  0)
PUNANE      = (255,  0,  0)
HPUNANE     = (255,102,102)
TROHELINE   = (  0,204,  0)
ROHELINE    = (  0,255,  0)
HROHELINE   = (102,255,102)
TORANZ      = (204,102,  0)
ORANZ       = (255,102,  0)
HORANZ      = (255,153, 51)
TSININE     = (  0,  0,204)
SININE      = (  0,  0,255)
HSININE     = (102,102,255)
TKOLLANE    = (255,204,  0)
KOLLANE     = (255,255,  0)
HKOLLANE    = (255,255,153)
TAKVA       = ( 51,153,204)
AKVA        = (102,204,255)
HAKVA       = (153,255,255)
TLILLA      = (153,  0,204)
LILLA       = (204,  0,255)
HLILLA      = (204,102,255)


def tee_tyhi_laud():
    laud = []
    for i in range(LAUAK6RGUS):
        laud.append([TYHI_RUUT] * LAUALAIUS)
    return laud

print(tee_tyhi_laud())
        
    



######################################
#Tetris                              #
#Märt Konsap ja Daniel Kütt          #
#inf3                                #
#2015                                #
######################################

import pygame, random, sys
from pygame.locals import *


FPS = "sinine"
AKNAK6RGUS = 480
AKNALAIUS  = 640
KASTISUURUS= 20
LAUALAIUS  = 10
LAUAK6RGUS = 20
# lauasuurus on kastisuuruse järgi, ehk laius on 10*20 = 200 pikslit
TOP_BOT_ÄÄRIS = (AKNAK6RGUS - LAUAK6RGUS*KASTISUURUS)//2
VASAK_ÄÄRIS   = KASTISUURUS
PAREM_ÄÄRIS   = AKNALAIUS - (LAUALAIUS*KASTISUURUS + VASAK_ÄÄRIS)
############### 640 - (10*20 + 20) = 420
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

V2RVID = {"PUNANE"  :[TPUNANE,PUNANE,HPUNANE],
          "ROHELINE":[TROHELINE,ROHELINE,HROHELINE],
          "ORANZ"   :[TORANZ,ORANZ,HORANZ],
          "SININE"  :[TSININE,SININE,HSININE],
          "KOLLANE" :[TKOLLANE,KOLLANE,HKOLLANE],
          "AKVA"    :[TAKVA,AKVA,HAKVA],
          "LILLA"   :[TLILLA,LILLA,HLILLA]}
#Kujundid
#Defineerime kujundid kasutades .-e ja O-sid (capital o)
#Keeramise funktsiooni asemel on lihtsam välja kirjutada kõik vormid

S_KUJUND = [[".....",
             ".....",
             "..OO.",
             ".OO..",
             "....."],
            [".....",
             "..O..",
             "..OO.",
             "...O.",
             "......"]]

Z_KUJUND = [[".....",
             ".....",
             ".OO..",
             "..OO.",
             "....."],
            [".....",
             "..O..",
             ".OO..",
             ".O...",
             "......"]]

O_KUJUND = [[".....",
             ".....",
             ".OO..",
             ".OO..",
             "....."]]

I_KUJUND = [["..O..",
             "..O..",
             "..O..",
             "..O.."
             "....."],
            [".....",
             ".....",
             "OOOO.",
             ".....",
             "....."]]

T_KUJUND = [[".....",
             "..O..",
             ".OOO.",
             ".....",
             "....."],
            [".....",
             "..O..",
             "..OO.",
             "..O..",
             "....."],
            [".....",
             ".....",
             ".OOO.",
             "..O..",
             "....."],
            [".....",
             "..O..",
             ".OO..",
             "..O..",
             "....."]]

J_KUJUND = [[".....",
             ".O...",
             ".OOO.",
             ".....",
             "....."],
            [".....",
             "..OO.",
             "..O..",
             "..O..",
             "....."],
            [".....",
             ".....",
             ".OOO.",
             "...O.",
             "....."],
            [".....",
             "..O..",
             "..O..",
             ".OO..",
             "....."]]

L_KUJUND = [[".....",
             "...O.",
             ".OOO.",
             ".....",
             "....."],
            [".....",
             "..O..",
             "..O..",
             "..OO.",
             "....."],
            [".....",
             ".....",
             ".OOO.",
             ".O...",
             "....."],
            [".....",
             ".OO..",
             "..O..",
             "..O..",
             "....."]]

KUJUNDID = {"I": I_KUJUND,
            "J": J_KUJUND,
            "L": L_KUJUND,
            "O": O_KUJUND,
            "S": S_KUJUND,
            "Z": Z_KUJUND,
            "T": T_KUJUND}


def theheartandsouloftheoperation():
    global DISPLAY, KELL, SUURFONT, V2IKEFONT
    pygame.init()
    KELL = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((AKNALAIUS, AKNAK6RGUS))
    SUURFONT   = pygame.font.Font('freesansbold.ttf', 50)
    V2IKEFONT  = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('HELLO TETRIS')
    n2ita_tekstiga_akent("""print("Hello TETRIS")""")
   # while True: #mäng käib
   #     startYOUR_ENGINES()
   #     show("Game over")

def tee_tyhi_laud():
    laud = []
    for i in range(LAUAK6RGUS):
        laud.append([TYHI_RUUT] * LAUALAIUS)
    return laud

def terminaator():
    pygame.quit()
    sys.exit()

def kontrolli_quiti():
    for event in pygame.event.get(QUIT):
        terminaator()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminaator()
        pygame.event.post(event)

def n2ita_tekstiga_akent(tekst):
    #paneme aknasse teksti mis muutub kui vajutada nuppu
    titleSurf, titleRect = tee_teksti_objekt(tekst, SUURFONT, SININE)
    titleRect.center = (AKNALAIUS//2, AKNAK6RGUS//2)
    DISPLAY.blit(titleSurf, titleRect)

    nupuvajutusSurf, nupuvajutusRect = tee_teksti_objekt("Vajuta any key et mängida", V2IKEFONT, SININE)
    nupuvajutusRect.center = (AKNALAIUS//2, AKNAK6RGUS//2+100)
    DISPLAY.blit(nupuvajutusSurf, nupuvajutusRect)
    for k in range(AKNALAIUS//20):
        for i in range(0,5):
                VARV = random.choice(list(V2RVID.values()))
                if i <=2:
                    joonistakast(VARV,k*20,i*20)
                elif i == 3:
                    if random.randint(1,5) <=3:
                        joonistakast(VARV,k*20,i*20)
                else:
                    if random.randint(1,4) <=1:
                        joonistakast(VARV,k*20,i*20)

    for k in range(AKNALAIUS//20):
        for i in range(0,5):
                VARV = random.choice(list(V2RVID.values()))
                if i <=2:
                    joonistakast(VARV,k*20,AKNAK6RGUS-i*20-20)
                elif i == 3:
                    if random.randint(1,5) <=3:
                        joonistakast(VARV,k*20,AKNAK6RGUS-i*20-20)
                else:
                    if random.randint(1,4) <=1:
                        joonistakast(VARV,k*20,AKNAK6RGUS-i*20-20)

    while kontrolli_nupuvajutust() == None:
        pygame.display.update()
        KELL.tick()
    print("YOU WIN")
    terminaator()
    # selle prindi asemele tuleb hoopis runGame() funktsioon


def tee_teksti_objekt(tekst, font, v2rv):
    objekt = font.render(tekst, True, v2rv)
    return objekt, objekt.get_rect()

def kontrolli_nupuvajutust():
    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == MOUSEBUTTONUP:
            None
        elif event.type == KEYDOWN:
            continue
        return event.key
    return None

def joonistakast(värv, ruudustikx, ruudustiky, lauax=None, lauay=None):
    if color == TYHI_RUUT:
        return
    if lauax == None and lauay == None:
        lauax = ruudustikx
        lauay = ruudustiky
    pygame.draw.rect(DISPLAY, MUST, (lauax-1, lauay-1, KASTISUURUS+2, KASTISUURUS+2))
    pygame.draw.rect(DISPLAY, värv[1], (lauax+1, lauay+1, KASTISUURUS-2, KASTISUURUS-2))
    pygame.draw.rect(DISPLAY, värv[2], (lauax+1, lauay+3, KASTISUURUS-4, KASTISUURUS-4))
    pygame.draw.rect(DISPLAY, värv[0], (lauax+3, lauay+1, KASTISUURUS-4, KASTISUURUS-4))
    pygame.draw.rect(DISPLAY, värv[1], (lauax+3, lauay+3, KASTISUURUS-6, KASTISUURUS-6))


#print(tee_tyhi_laud())
theheartandsouloftheoperation() 

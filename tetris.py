######################################
#Tetris                              #
#Märt Konsap ja Daniel Kütt          #
#inf3                                #
#2015                                #
######################################

import pygame, random, sys
from pygame.locals import *


FPS = 1
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

TAUSTAV2RV = HALL

V2RVID = {"PUNANE"  :[TPUNANE,PUNANE,HPUNANE],
          "ROHELINE":[TROHELINE,ROHELINE,HROHELINE],
          "ORANZ"   :[TORANZ,ORANZ,HORANZ],
          "SININE"  :[TSININE,SININE,HSININE],
          "KOLLANE" :[TKOLLANE,KOLLANE,HKOLLANE],
          "AKVA"    :[TAKVA,AKVA,HAKVA],
          "LILLA"   :[TLILLA,LILLA,HLILLA],
          "."       :"."}
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
    #print("YOU WIN")
    #terminaator()
    while True: #mäng käib
        startYOUR_ENGINES()
        n2ita_tekstiga_akent("Game over")

def startYOUR_ENGINES():
    # Muutujad alguses
    laud = tee_tyhi_laud()
    seis = 0
    level = 1 # tuleb teha funktsiooniga, et arvutaks

    # Mängu loop
    while True:

        # Joonistamisfunktsioonid
        DISPLAY.fill(TAUSTAV2RV)
        joonistalaud(laud)
        joonistaseis(seis, level)
        #joonistauusklots(uusklots)
        #if langevklots != None:
        #   joonistaklots(langevklots)
        
        # pygame.display.update()
        KELL.tick(FPS)

def tee_tyhi_laud():
    laud = []
    for i in range(LAUAK6RGUS):
        laud.append([TYHI_RUUT] * LAUALAIUS)
    print(laud)
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
    titleSurf, titleRect = tee_teksti_objekt(tekst, SUURFONT, VALGE)
    titleRect.center = (AKNALAIUS//2, AKNAK6RGUS//2)
    DISPLAY.blit(titleSurf, titleRect)

    nupuvajutusSurf, nupuvajutusRect = tee_teksti_objekt("Vajuta any key et mängida", V2IKEFONT, VALGE)
    nupuvajutusRect.center = (AKNALAIUS//2, AKNAK6RGUS//2+100)
    DISPLAY.blit(nupuvajutusSurf, nupuvajutusRect)
    
    for k in range(AKNALAIUS//20):
        for i in range(0,5):
                while True:
                    VARV = random.choice(list(V2RVID.values()))
                    if VARV != TYHI_RUUT:
                        break
                if i <=2:
                    joonistakast(VARV,0,0,k*20,i*20)
                elif i == 3:
                    if random.randint(1,5) <=3:
                        joonistakast(VARV,0,0,k*20,i*20)
                else:
                    if random.randint(1,4) <=1:
                        joonistakast(VARV,0,0,k*20,i*20)

    for k in range(AKNALAIUS//20):
        for i in range(0,5):
                while True:
                    VARV = random.choice(list(V2RVID.values()))
                    if VARV != TYHI_RUUT:
                        break
                if i <=2:
                    joonistakast(VARV,0,0,k*20,AKNAK6RGUS-i*20-20)
                elif i == 3:
                    if random.randint(1,5) <=3:
                        joonistakast(VARV,0,0,k*20,AKNAK6RGUS-i*20-20)
                else:
                    if random.randint(1,4) <=1:
                        joonistakast(VARV,0,0,k*20,AKNAK6RGUS-i*20-20)

    while kontrolli_nupuvajutust() == None:
        pygame.display.update()
        KELL.tick()


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

#See joonistab ilusa kasti
def joonistakast(v2rv, ruudustikx, ruudustiky, lauax=None, lauay=None):
    if v2rv == TYHI_RUUT:
        return
    if lauax == None and lauay == None:
        lauax, lauay = ruudustikTOlaud(ruudustikx, ruudustiky)
    pygame.draw.rect(DISPLAY, MUST, (lauax-1, lauay-1, KASTISUURUS+2, KASTISUURUS+2))
    pygame.draw.rect(DISPLAY, v2rv[1], (lauax+1, lauay+1, KASTISUURUS-2, KASTISUURUS-2))
    pygame.draw.rect(DISPLAY, v2rv[2], (lauax+1, lauay+3, KASTISUURUS-4, KASTISUURUS-4))
    pygame.draw.rect(DISPLAY, v2rv[0], (lauax+3, lauay+1, KASTISUURUS-4, KASTISUURUS-4))
    pygame.draw.rect(DISPLAY, v2rv[1], (lauax+3, lauay+3, KASTISUURUS-6, KASTISUURUS-6))

def joonistalaud(m2ngulaud):
    #Ilusad ajsad ümber mängulaua on vaja ise leiutada

    for y in range(LAUAK6RGUS):
        for x in range(LAUALAIUS):
            joonistakast(V2RVID[m2ngulaud[y][x]],x,y)

def joonistaseis(skoor, level):
    skoorSurf = V2IKEFONT.render("Skoor: %s" % skoor, True, VALGE)
    skoorRect = skoorSurf.get_rect()
    skoorRect.topleft = (AKNALAIUS - 100, 20) # ajutine
    DISPLAY.blit(skoorSurf, skoorRect)

    levelSurf = V2IKEFONT.render("Level: %s" % level, True, VALGE)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (AKNALAIUS - 100, 50) # see on ajutine
    DISPLAY.blit(levelSurf, levelRect)


def ruudustikTOlaud(ruudustikx, ruudustiky):
    lauax = VASAK_ÄÄRIS + (ruudustikx * KASTISUURUS)
    lauay = TOP_BOT_ÄÄRIS + (ruudustiky * KASTISUURUS)
    return lauax, lauay

#print(tee_tyhi_laud())
theheartandsouloftheoperation() 

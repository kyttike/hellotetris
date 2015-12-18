######################################
#Tetris                              #
#Märt Konsap ja Daniel Kütt          #
#inf3                                #
#2015                                #
######################################

import pygame, random, sys, time
from pygame.locals import *


FPS = 25
AKNAK6RGUS = 480
AKNALAIUS  = 650
KASTISUURUS= 25
LAUALAIUS  = 10
LAUAK6RGUS = 18
TOP_BOT_ÄÄRIS = (AKNAK6RGUS - LAUAK6RGUS*KASTISUURUS)//2
VASAK_ÄÄRIS   = KASTISUURUS
PAREM_ÄÄRIS   = AKNALAIUS - (LAUALAIUS*KASTISUURUS + VASAK_ÄÄRIS)
TYHI_RUUT       = "."
KUJUNDILAIUS    = 5
KUJUNDIK6RGUS   = 5

KYLGSAGEDUS = 0.15
ALLAHSAGEDUS = 0.1

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

TEKSTIV2RV  = MUST
TAUSTAV2RV  = (221,238,255)
LAUAV2RV    = (195,213,234)
LAUA22R     = (102,119,153)


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
             "..O..",
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

KUJUNDV2RV = {"I": "ORANZ",
              "J": "LILLA",
              "L": "SININE",
              "O": "PUNANE",
              "S": "AKVA",
              "Z": "ROHELINE",
              "T": "KOLLANE"}


def theheartandsouloftheoperation():
    global DISPLAY, KELL, SUURFONT, V2IKEFONT
    pygame.init()
    KELL = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((AKNALAIUS, AKNAK6RGUS))
    SUURFONT   = pygame.font.SysFont('impact', 50)
    V2IKEFONT  = pygame.font.SysFont('impact', 18)
    pygame.display.set_caption('HELLO TETRIS')
    n2ita_tekstiga_akent("""print("Hello TETRIS")""",VALGE)
    while True: #mäng käib
        startYOUR_ENGINES()
        DISPLAY.fill(MUST)
        n2ita_tekstiga_akent("Game over", VALGE, ("Skoor: " + str(skoor)))
        pygame.time.wait(500)


def startYOUR_ENGINES():
    global skoor
    laud = tee_tyhi_laud()
    allah_aeg = time.time()
    kylg_aeg = time.time()
    kukkumis_aeg = time.time()
    skoor = 0
    level, langemissagedus = arvuta_level_ja_langemissagedus(skoor)
    liigub_alla = False
    liigub_paremale = False
    liigub_vasakule = False

    langevklots = teeuusklots()
    j2rgmineklots = teeuusklots()
    
    # Mängu Uno Loop
    while True:
        if langevklots == None:
            langevklots = j2rgmineklots
            j2rgmineklots = teeuusklots()
            kukkumis_aeg = time.time()

            if not onsobivasend(laud, langevklots):
                return
        kontrolli_quiti()
        for event in pygame.event.get():
            if event.type == KEYUP:
                if (event.key == K_p):
                    DISPLAY.fill(TAUSTAV2RV)
                    n2ita_tekstiga_akent("""print("Hello PAUS")""",MUST)
                    kukkumis_aeg = time.time()
                    allah_aeg = time.time()
                    kylg_aeg = time.time()
                elif (event.key == K_LEFT or event.key == K_a):
                    liigub_vasakule = False
                elif (event.key == K_RIGHT or event.key == K_d):
                    liigub_paremale = False
                elif (event.key == K_DOWN or event.key == K_s):
                    liigub_alla = False

            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and onsobivasend(laud, langevklots, adjx=-1):
                    langevklots['x'] -= 1
                    liigub_vasakule = True
                    liigub_paremale = False
                    kylg_aeg = time.time()
                elif (event.key == K_RIGHT or event.key == K_d) and onsobivasend(laud, langevklots, adjx=1):
                    langevklots['x'] += 1
                    liigub_paremale = True
                    liigub_vasakule = False
                    kylg_aeg = time.time()
                elif (event.key == K_UP or event.key == K_w):
                    langevklots['asend'] = (langevklots['asend'] + 1) % len(KUJUNDID[langevklots['kuju']])
                    if not onsobivasend(laud, langevklots):
                        langevklots['asend'] = (langevklots['asend'] - 1) % len(KUJUNDID[langevklots['kuju']])
##                elif (event.key == K_q):
##                    langevklots['asend'] = (langevklots['asend'] - 1) % len(KUJUNDID[langevklots['kuju']])
##                    if not onsobivasend(laud, langevklots):
##                        langevklots['asend'] = (langevklots['asend'] + 1) % len(KUJUNDID[langevklots['kuju']])

                elif (event.key == K_DOWN or event.key == K_s):
                    liigub_alla = True
                    if onsobivasend(laud, langevklots, adjy = 1):
                        langevklots['y'] += 1
                    allah_aeg = time.time()

                elif event.key == K_SPACE:
                    liigub_alla = False
                    liigub_paremale = False
                    liigub_vasakule = False
                    for i in range(1, LAUAK6RGUS):
                        if not onsobivasend(laud, langevklots, adjy=i):
                            break
                    langevklots['y'] += i - 1
                    lisalauale(laud, langevklots)
                elif event.key == K_e:
                    liigub_alla = False
                    liigub_paremale = False
                    liigub_vasakule = False
                    for i in range(1, LAUALAIUS):
                        if not onsobivasend(laud, langevklots, adjx=i):
                            break
                    langevklots['x'] += i - 1
                elif event.key == K_q:
                    liigub_alla = False
                    liigub_paremale = False
                    liigub_vasakule = False
                    for i in range(1, LAUALAIUS):
                        if not onsobivasend(laud, langevklots, adjx=-i):
                            break
                    langevklots['x'] -= i -1
                    
                    
        if (liigub_vasakule or liigub_paremale) and time.time() - kylg_aeg > KYLGSAGEDUS:
            if liigub_vasakule and onsobivasend(laud, langevklots, adjx=-1):
                langevklots['x'] -= 1
            elif liigub_paremale and onsobivasend(laud, langevklots, adjx=1):
                langevklots['x'] += 1
            kylg_aeg = time.time()

        if liigub_alla and time.time() - allah_aeg > ALLAHSAGEDUS and onsobivasend(laud, langevklots, adjy=1):
            langevklots['y'] += 1
            allah_aeg = time.time()

        if time.time() - kukkumis_aeg > langemissagedus:
            if not onsobivasend(laud, langevklots, adjy=1):
                lisalauale(laud, langevklots)
                skoor += eemaldat2isread(laud)
                level, langemissagedus = arvuta_level_ja_langemissagedus(skoor)
                langevklots = None
            else:
                langevklots['y'] += 1
                kukkumis_aeg = time.time()
                
        # Joonistamisfunktsioonid
        DISPLAY.fill(TAUSTAV2RV)
        joonistalaud(laud)
        joonistaseis(skoor, level)
        joonistauusklots(j2rgmineklots)
        if langevklots != None:
           joonistaklots(langevklots)
        
        pygame.display.update()
        KELL.tick(FPS)

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

def n2ita_tekstiga_akent(tekst,v2rv,teinerida=None):
    #paneme aknasse teksti mis muutub kui vajutada nuppu
    titleSurf, titleRect = tee_teksti_objekt(tekst, SUURFONT, v2rv)
    titleRect.center = (AKNALAIUS//2, AKNAK6RGUS//2)
    DISPLAY.blit(titleSurf, titleRect)

    nupuvajutusSurf, nupuvajutusRect = tee_teksti_objekt("Vajuta any key et mängida", V2IKEFONT, v2rv)
    nupuvajutusRect.center = (AKNALAIUS//2, AKNAK6RGUS//2+80)
    DISPLAY.blit(nupuvajutusSurf, nupuvajutusRect)

    if teinerida != None:
        teineridaSurf, teineridaRect = tee_teksti_objekt(teinerida, V2IKEFONT, v2rv)
        teineridaRect.center = (AKNALAIUS//2, AKNAK6RGUS//2+40)
        DISPLAY.blit(teineridaSurf, teineridaRect) 
    
    for k in range(AKNALAIUS//KASTISUURUS+1):
        for i in range(0,5):
                while True:
                    VARV = random.choice(list(V2RVID.values()))
                    if VARV != TYHI_RUUT:
                        break
                if i <=2:
                    joonistakast(VARV,0,0,k*KASTISUURUS,i*KASTISUURUS)
                elif i == 3:
                    if random.randint(1,5) <=3:
                        joonistakast(VARV,0,0,k*KASTISUURUS,i*KASTISUURUS)
                else:
                    if random.randint(1,4) <=1:
                        joonistakast(VARV,0,0,k*KASTISUURUS,i*KASTISUURUS)

    for k in range(AKNALAIUS//KASTISUURUS+1):
        for i in range(0,5):
                while True:
                    VARV = random.choice(list(V2RVID.values()))
                    if VARV != TYHI_RUUT:
                        break
                if i <=2:
                    joonistakast(VARV,0,0,k*KASTISUURUS,AKNAK6RGUS-i*KASTISUURUS-KASTISUURUS)
                elif i == 3:
                    if random.randint(1,5) <=3:
                        joonistakast(VARV,0,0,k*KASTISUURUS,AKNAK6RGUS-i*KASTISUURUS-KASTISUURUS)
                else:
                    if random.randint(1,4) <=1:
                        joonistakast(VARV,0,0,k*KASTISUURUS,AKNAK6RGUS-i*KASTISUURUS-KASTISUURUS)

    while kontrolli_nupuvajutust() == None:
        pygame.display.update()
        KELL.tick()


def tee_teksti_objekt(tekst, font, v2rv):
    objekt = font.render(tekst, True, v2rv)
    return objekt, objekt.get_rect()

def teeuusklots():
    kuju = random.choice(list(KUJUNDID.keys()))
    uusklots = {"kuju": kuju,
                "asend": random.randint(0, len(KUJUNDID[kuju])-1),
                "x": int(LAUALAIUS / 2) - int(KUJUNDILAIUS / 2),
                "y": 0 - int(KUJUNDIK6RGUS / 2),
                "v2rv": KUJUNDV2RV[kuju]}
    return uusklots

def kontrolli_nupuvajutust():
    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == MOUSEBUTTONUP:
            None
        elif event.key == K_ESCAPE:
            terminaator()
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
    pygame.draw.rect(DISPLAY, v2rv[0], (lauax+1, lauay+3, KASTISUURUS-4, KASTISUURUS-4))
    pygame.draw.rect(DISPLAY, v2rv[2], (lauax+3, lauay+1, KASTISUURUS-4, KASTISUURUS-4))
    pygame.draw.rect(DISPLAY, v2rv[1], (lauax+3, lauay+3, KASTISUURUS-6, KASTISUURUS-6))

def joonistalaud(m2ngulaud):
    pygame.draw.rect(DISPLAY, LAUA22R, (VASAK_ÄÄRIS-4 ,TOP_BOT_ÄÄRIS-4, (LAUALAIUS * KASTISUURUS)+8, (LAUAK6RGUS * KASTISUURUS)+8), 0)
    pygame.draw.rect(DISPLAY, LAUAV2RV, (VASAK_ÄÄRIS ,TOP_BOT_ÄÄRIS, (LAUALAIUS * KASTISUURUS), (LAUAK6RGUS * KASTISUURUS)), 0)
    for x in range(LAUALAIUS):
        for y in range(LAUAK6RGUS):
            joonistakast(V2RVID[m2ngulaud[y][x]],x,y)

def joonistaseis(skoor, level):
    skoorSurf = V2IKEFONT.render("Skoor: %s" % skoor, True, TEKSTIV2RV)
    skoorRect = skoorSurf.get_rect()
    skoorRect.topleft = (AKNALAIUS - PAREM_ÄÄRIS+20, 20) # ajutine
    DISPLAY.blit(skoorSurf, skoorRect)

    levelSurf = V2IKEFONT.render("Level: %s" % level, True, TEKSTIV2RV)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (AKNALAIUS - PAREM_ÄÄRIS+20, 50) # see on ajutine
    DISPLAY.blit(levelSurf, levelRect)

########
##    readSurf = V2IKEFONT.render("Read: %s" % read, True, VALGE)
##    readRect = readSurf.get_rect()
##    readRect.topleft = (AKNALAIUS - PAREM_ÄÄRIS+20, 80) # see on ajutine
##    DISPLAY.blit(readSurf, readRect)
########

def joonistaklots(klots, lauax=None, lauay=None):
    joonistan = KUJUNDID[klots["kuju"]][klots["asend"]]
    if lauax == None and lauay == None:
        lauax, lauay = ruudustikTOlaud(klots["x"],klots["y"])

    for x in range(KUJUNDILAIUS):
        for y in range(KUJUNDIK6RGUS):
            if joonistan[y][x] != TYHI_RUUT:
                joonistakast(V2RVID[klots["v2rv"]], None, None, lauax + (x*KASTISUURUS), lauay + (y*KASTISUURUS))

def joonistauusklots(klots):
    j2rgmineSurf = V2IKEFONT.render("Järgmine:", True, TEKSTIV2RV)
    j2rgmineRect = j2rgmineSurf.get_rect()
    j2rgmineRect.topleft = (AKNALAIUS - PAREM_ÄÄRIS+20, 80)
    DISPLAY.blit(j2rgmineSurf,j2rgmineRect)
    joonistaklots(klots,(AKNALAIUS - PAREM_ÄÄRIS+20), 110)

def lisalauale(laud, klots):
    for x in range(KUJUNDILAIUS):
        for y in range(KUJUNDIK6RGUS):
            if KUJUNDID[klots['kuju']][klots['asend']][y][x] != TYHI_RUUT:
                laud[y + klots['y']][x + klots['x']] = klots['v2rv']

def ruudustikTOlaud(ruudustikx, ruudustiky):
    lauax = VASAK_ÄÄRIS + (ruudustikx * KASTISUURUS)
    lauay = TOP_BOT_ÄÄRIS + (ruudustiky * KASTISUURUS)
    return lauax, lauay

def onlaual(x, y):
    return x >= 0 and x < LAUALAIUS and y < LAUAK6RGUS

def onsobivasend(laud, klots, adjx=0, adjy=0):
    for x in range(KUJUNDILAIUS):
        for y in range(KUJUNDIK6RGUS):
            lauastk6rgemal = y + klots['y'] + adjy < 0
            if lauastk6rgemal or KUJUNDID[klots['kuju']][klots["asend"]][y][x] == TYHI_RUUT:
                continue
            if not onlaual(x + klots['x'] + adjx, y + klots['y'] + adjy):
                return False
            if laud[y + klots['y'] + adjy][x + klots['x'] + adjx] != TYHI_RUUT:
                return False
    return True
    

def arvuta_level_ja_langemissagedus(skoor):
    #langemissagedus on sekundites, et
    #mitu sekundit kulub enne kui klots liigub ühe ruudu võrra
    level = int(skoor//10)+1
    langemissagedus = 0.47 - (level * 0.02)
    return level, langemissagedus



def ont2isrida(laud, y):
    for x in range(LAUALAIUS):
        if laud[y][x] == TYHI_RUUT:
            return False
    return True

def eemaldat2isread(laud):
    eemaldatud = 0
    y = LAUAK6RGUS - 1
    while y >= 0:
        if ont2isrida(laud, y):
            for yleminealla in range(y, 0, -1):
                for x in range(LAUALAIUS):
                    laud[yleminealla][x] = laud[yleminealla-1][x]
            for x in range(LAUALAIUS):
                laud[0][x] = TYHI_RUUT
            eemaldatud += 1
        else:
            y -= 1
    return eemaldatud

theheartandsouloftheoperation() 

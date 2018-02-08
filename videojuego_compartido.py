# videogame
# my first video game for school project 
#-*- coding: utf-8 -*-
import pygame, sys

from pygame.locals import *
import random
import math

pygame.init()

pygame.key.set_repeat(1,24)
reloj = pygame.time.Clock()

ancho=500
alto =250

visor = pygame.display.set_mode((ancho,alto))

pygame.display.set_caption("Sprite")

bicho = pygame.image.load('Ken.png')
fan = pygame.image.load('fantasma.png')

def escalera(posx,posy,K_RIGHT,K_LEFT, escalones=[40,80,120,160]):
    if posx >= escalones[0] and posx < escalones[1]:
        if K_RIGHT == 1:
            posy -=2
        if K_LEFT == 1:
            posy +=2
    if posx > escalones[2] and posx <= escalones[3]:
        if K_RIGHT == 1:
            posy +=2
        if K_LEFT == 1:
            posy -=2
    return posy

#fasemov=0

#pos=0
listadisparo=[]
e = 0
#direccion = "derecha"
personaje1={"pos":0, "posy":150, "fasemov":0,
"movbichoder":[(42,100,77,100), (165,100,77,100),(282,100,77,100),(400,100,77,100)],
"movbichoizq":[(42,200,77,100), (165,200,77,100),(282,200,77,100),(400,200,77,100)],
"movbicho": [(42,100,77,100), (165,100,77,100),(282,100,77,100),(400,100,77,100)], "posy_ini": 150}

fantasma={"posx":125, "posy":75, "fasemov":0, "movbicho": [(0,0,60,75),(0,75,60,75),(0,150,60,75),(0,225,60,75),(0,300,60,75),(0,375,60,75),
(0,450,60,75),(0,525,60,75),(0,600,60,75),(0,675,60,75),(0,750,60,75),(0,825,60,75),(0,900,60,75),(0,975,60,75),(0,1050,60,75),(0,1125,60,75),
(0,1200,60,75),(0,1275,60,75),(0,1350,60,75),(0,1425,60,75)], "sumarx": 1.5, "sumary": 1.5}

plataformas=[range(50,100),range(150,200)]


subir=range(0,120,3)
bajar=range(117,-1,-3)
contador_salto = 0
posicion_inicial_vertical = 150
interruptor_grave = "0"
interruptor_grave2 = "0"

salto=10


def funfantasma(posx,posy,sumarx,sumary,fasemov,movbicho):
    anchobicho=53
    altobicho=65

    fasemov += 1
    if fasemov > len(movbicho)-1:
        fasemov = 0
    if posx > ancho-anchobicho:
        sumarx = random.uniform(-3,0)
        lado = random.randrange(0,2)
        if lado == 0:
            sumary = math.sqrt(3**2 - abs(sumarx)**2)
        else:
            sumary = -math.sqrt(3**2 - abs(sumarx)**2)

    if posx < 0:
        sumarx = random.uniform(0,3)
        lado = random.randrange(0,2)
        if lado == 0:
            sumary = math.sqrt(3**2 - sumarx**2)
        else:
            sumary = -math.sqrt(3**2 - sumarx**2)

    if posy > alto-altobicho:
        sumary = random.uniform(-3,0)
        lado = random.randrange(0,2)
        if lado == 0:
            sumarx = math.sqrt(3**2 - abs(sumary)**2)
        else:
            sumarx = -math.sqrt(3**2 - abs(sumary)**2)

    if posy < 0:
        sumary = random.uniform(0,3)
        lado = random.randrange(0,2)
        if lado == 0:
            sumarx = math.sqrt(3**2 - sumary**2)
        else:
            sumarx = -math.sqrt(3**2 - sumary**2)

    posx += sumarx
    posy += sumary
    return posx, posy, sumarx, sumary, fasemov

def proyectil(pos,movbicho,movbichoder):
    if movbicho == movbichoder:
        disparo={'x': 0, 'y': 195, 'bala': pygame.image.load('llama1.png'), 'imagbala':[(0,0,33,33),(33,0,33,33),(0,33,33,33),(33,33,33,33)]}
        disparo['x'] = pos
    else:
        disparo={'x': 0, 'y': 150, 'bala': pygame.image.load('llama1.png'), 'imagbala':[(0,66,33,33),(33,66,33,33),(0,99,33,33),(33,99,33,33)]}
        disparo['x'] = pos
    return disparo

while True:
    teclasPulsadas = pygame.key.get_pressed()
    if interruptor_grave == "1":
        interruptor_grave2 = "1"
        personaje1["posy"] -= salto
        salto -= 1
        print personaje1['posy'],
        print personaje1['posy_ini']
        if personaje1["posy"] == personaje1["posy_ini"]:
            interruptor_grave = "0"
            salto = 10
            interruptor_grave2 = "0"
            print personaje1['posy']

    	'''contador_salto += 1
    	if contador_salto < len(subir):
    		personaje1["posy"] = posicion_inicial_vertical - subir[contador_salto]
    	else:
    		personaje1["posy"] = posicion_inicial_vertical - bajar[contador_salto - len(subir)]
        if contador_salto == len(subir)-1 + len(bajar):
    		interruptor_grave = 0
    		contador_salto = 0'''

        pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



        if teclasPulsadas[K_LEFT]:
            personaje1["movbicho"] = personaje1["movbichoizq"]
            personaje1["pos"] -= 1
            personaje1["fasemov"] -= 1
            if personaje1["fasemov"] < 0:
               personaje1["fasemov"] = len(personaje1["movbicho"])-1
        if teclasPulsadas[K_RIGHT]:
            personaje1["movbicho"] = personaje1["movbichoder"]
            personaje1["pos"]+=1
            personaje1["fasemov"] += 1
            if personaje1["fasemov"] > len(personaje1["movbicho"])-1:
                personaje1["fasemov"] = 0
        if teclasPulsadas[K_UP] and interruptor_grave2 == "0":
            interruptor_grave = "1"
            personaje1["posy_ini"] = personaje1["posy"]
        if teclasPulsadas[K_q]:
            disparo = proyectil(personaje1["pos"],personaje1["movbicho"],personaje1["movbichoder"])
            listadisparo.append(disparo)

        personaje1["posy"] = escalera(personaje1["pos"],personaje1["posy"],teclasPulsadas[K_RIGHT],teclasPulsadas[K_LEFT])

    for i in listadisparo:
        if i['x'] > ancho:
            listadisparo.remove(i)
        if i['x'] < 0:
            listadisparo.remove(i)
    for i in listadisparo:
        if i['imagbala'] == [(0,0,33,33),(33,0,33,33),(0,33,33,33),(33,33,33,33)]:
            i['x'] += 10
        else:
            i['x'] -= 10

    fantasma["posx"], fantasma["posy"], fantasma["sumarx"], fantasma["sumary"], fantasma["fasemov"] = funfantasma(fantasma["posx"],fantasma["posy"],fantasma["sumarx"],fantasma["sumary"],fantasma["fasemov"],fantasma["movbicho"])


    visor.fill((255,255,255))
    visor.blit(bicho, (personaje1["pos"],personaje1["posy"]), personaje1["movbicho"][personaje1["fasemov"]])
    for i in listadisparo:
        if e == len(disparo['imagbala']):
            e = 0
        visor.blit(i['bala'],(i['x'],i['y']), i['imagbala'][e])
        e += 1
    visor.blit(fan, (fantasma["posx"], fantasma["posy"]), fantasma["movbicho"][fantasma["fasemov"]])

    reloj.tick(30)
    pygame.display.update()

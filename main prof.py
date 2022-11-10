import random
import time

from pygame import Rect
from pygame.math import Vector2

import core
from prototype import drawTir, drawPlayer


def setup():
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]
    core.memory("position",Vector2(400,400))
    core.memory("vitesse",Vector2(-0.00001,0))

    core.memory("projectiles",[])
    core.memory("target",Rect(random.randint(0,core.WINDOW_SIZE[0]),random.randint(0,core.WINDOW_SIZE[1]), 20 ,20))


def run():
    core.cleanScreen()

    #TIR
    if core.getKeyPressList("SPACE") :
        if len(core.memory("projectiles")) > 0:
            if  time.time() - core.memory("projectiles")[-1]["startTime"] > 0.01:
                 creationProjectile()
        else:
            creationProjectile()

    #DEPLACEMENT
    core.memory("position", core.memory("position")+core.memory("vitesse")  )
    for p in core.memory("projectiles"):
        p["position"]=p["position"] + p["vitesse"]



    #CONTROL
    if core.getKeyPressList("z"):
        core.memory("vitesse").scale_to_length(  core.memory("vitesse").length() + 1  )

    if core.getKeyPressList('d'):
        core.memory("vitesse", core.memory("vitesse").rotate(1))

    #DESSIN
    core.Draw.rect((255,0,0),core.memory('target'))

    for p in core.memory("projectiles"):
        drawTir(p)

    drawPlayer()

    #Collision
    for p in core.memory("projectiles"):
        if core.memory('target').collidepoint(p["position"].x,p["position"].y):
            core.memory("target",Rect(random.randint(0,core.WINDOW_SIZE[0]),random.randint(0,core.WINDOW_SIZE[1]), 20 ,20))


    #clean
    for p in core.memory("projectiles"):
        if p["position"].x > core.WINDOW_SIZE[0] or p["position"].y > core.WINDOW_SIZE[1] or p["position"].x < 0 or p["position"].y < 0 :
            core.memory("projectiles").remove(p)




def creationProjectile():
    vitesse = Vector2(core.memory("vitesse"))
    vitesse.scale_to_length(10)
    d = {"position": Vector2(core.memory("position")), "vitesse": vitesse, "rayon": 5, "startTime": time.time()}
    core.memory("projectiles").append(d)


core.main(setup, run)
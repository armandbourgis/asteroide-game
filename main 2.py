import random
import time

from pygame import Rect
from pygame.math import Vector2

import core

def setup() :
    print("Setup START--------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]
    print("Setup END----------")
    core.memory("vitesse", Vector2(0, 1))
    core.memory("position", Vector2(400, 400))
    core.memory("projectiles", [])
    core.memory("target", Rect(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]), 20, 20))


def run():
    core.cleanScreen()

    # TIR
    if core.getKeyPressList("SPACE"):
        if len(core.memory("projectiles")) > 0:
            if time.time() - core.memory("projectiles")[-1]["startTime"] > 1:
                creationProjectile()
        else:
            creationProjectile()

    #DEPLACEMENT
    core.memory("position", core.memory("position")+core.memory("vitesse"))
    for p in core.memory("projectiles") :
        p["position"] = p["position"] + p["vitesse"]


    #Update
    core.memory("position", core.memory("position") + core.memory("vitesse"))

    #control
    if core.getKeyPressList("z") :
        core.memory("vitesse").scale_to_length(core.memory("vitesse").length()+0.2)

    if core.getKeyPressList("d") :
        core.memory("vitesse", core.memory("vitesse").rotate(5))
    if core.getKeyPressList("q") :
        core.memory("vitesse", core.memory("vitesse").rotate(-5))

    #DESSIN
    core.Draw.rect((255,0,0),core.memory('target'))

    for proj in core.memory("projectiles"):
        core.Draw.circle(proj["color"], proj["position"], proj["rayon"])

    #Collision
    for p in core.memory("projectiles"):
        if core.memory('target').collidepoint(p["position"].x,p["position"].y):
            core.memory("target",Rect(random.randint(0,core.WINDOW_SIZE[0]),random.randint(0,core.WINDOW_SIZE[1]), 20 ,20))


    #clean
    for p in core.memory("projectiles"):
        if p["position"].x > core.WINDOW_SIZE[0] or p["position"].y > core.WINDOW_SIZE[1] or p["position"].x < 0 or p["position"].y < 0 :
            core.memory("projectiles").remove(p)




    #print(core.memory("vitesse"))

    vectP2 = Vector2(core.memory("vitesse"))

    vectP2.scale_to_length(40)
    p2=core.memory("position") + vectP2


    vecP1 = core.memory("vitesse")
    vecP1 = vecP1.rotate(90)
    vecP1.scale_to_length(10)
    p1 = core.memory("position") + vecP1

    vecP3 = core.memory("vitesse")
    vecP3 = vecP3.rotate(-90)
    vecP3.scale_to_length(10)
    p3 = core.memory("position") + vecP3
    core.Draw.polygon((255, 0, 0), (p1, p2, p3))


def creationProjectile():
    p = Vector2(core.memory("position"))
    v = Vector2(core.memory("vitesse"))
    v.scale_to_length(core.memory("vitesse").length() + 10)
    r = 10
    c = (255, 255, 255)
    startTime = time.time()

    proj = {"position": p, "vitesse": v, "rayon": r, 'startTime': startTime, "color": c}
    core.memory("projectiles").append(proj)



core.main(setup, run)
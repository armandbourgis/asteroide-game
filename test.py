import random
from pygame.math import Vector2, Vector3
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 600]

    core.memory("bobPosition", Vector2(0, 0))
    core.memory("origine",Vector2(400,300))
    core.memory("bobHistorique",[])

    print("Setup END-----------")




def run():
#    core.cleanScreen()
    if core.getKeyPressList("r"):
        core.memory("bobPosition", Vector2(0, 0))

    #DESSIN
    core.Draw.circle((255,0,0),core.memory("bobPosition") + core.memory("origine"),7)

    #DEPLACEMENT
    posx = core.memory("bobPosition").x
    posy = core.memory("bobPosition").y
    core.memory("bobPosition", Vector2(posx, posy))
    if core.getKeyPressList("z"):
        core.memory("bobPosition", Vector2(posx, posy-7))
    if core.getKeyPressList("s"):
        core.memory("bobPosition", Vector2(posx, posy+7))
    if core.getKeyPressList("q"):
        core.memory("bobPosition", Vector2(posx-7, posy))
    if core.getKeyPressList("d"):
        core.memory("bobPosition", Vector2(posx+7, posy))
#    vel = Vector2(a,b)
#    posx = core.memory("bobPosition").x + vel.x
#    posy = core.memory("bobPosition").y + vel.y
#    core.memory("bobPosition", Vector2(posx, posy))
#    X=vel.length()
#    core.memory("bobHistorique").append(X)
    core.printMemory()

    print("moyenne",sum(core.memory("bobHistorique"))/len(core.memory("bobHistorique")))
    print("distance totale",sum(core.memory("bobHistorique")))



core.main(setup, run)



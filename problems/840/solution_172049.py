import math
def bolos(farinha,ovos,leite):
    farinha= math.floor(farinha/2)
    ovos = math.floor(ovos/3)
    leite = math.floor(leite/5)
    minimo = farinha
    if (ovos<minimo):
        minimo=ovos
        return minimo
    if (leite<minimo):
        minimo=leite
        return minimo
    else:
        return minimo
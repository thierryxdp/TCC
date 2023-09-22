import math
def bolos(a,b,c):
    farinha=a/2
    ovos=b/3
    leite=c/5
    if farinha<leite or farinha<ovos:
        return math.floor(farinha)
    else:
        if ovos<leite or ovos<farinha:
            return math.floor(ovos)
        else:
            return math.floor(leite)
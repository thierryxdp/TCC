import math
def bolos(xicaras,ovos,leite):
    A=math.floor(xicaras/2)
    B=math.floor(ovos/3)
    C=math.floor(leite/5)
    if A<=B and A<=C:
        return A
    elif B<=A and B<=C:
        return B
    else:
        return C
math import
def bolos(xicaras,ovos,leite):
    A=xicaras/2
    B=ovos/3
    C=leite/5
    if A<=B and A<=C:
        return math.floor(A)
    elif B<=A and B<=C:
        return math.floor(B)
    else:
        return math.floor(C)
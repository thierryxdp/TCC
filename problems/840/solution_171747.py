def bolos(xicaras,ovos,leite):
    A=xicaras/2
    B=ovos/3
    C=leite/5
    if A<=B and A<=C:
        return A
    elif B<=A and B<=C:
        return B
    else:
        return C
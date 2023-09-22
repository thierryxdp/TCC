def seg(voltas):
    X=0
    Z=voltas[0][0]
    while X<len(voltas):
        Y=0
        while Y<len(voltas[0]):
            if voltas[X][Y]<Z:
                Z=voltas[X][Y]
            Y=Y+1
        X=X+1
    return Z
#
def corredor(voltas):
    X=0
    Z=seg(voltas)
    W=1
    Y=0
    while X<len(voltas) and voltas[X][Y]!=Z:
        while Y<len(voltas[0]):
            if Z==voltas[X][Y]:
                W=W+X
            Y=Y+1
        X=X+1
        Y=0
    return W
#
def melhor_volta(voltas):
    X=0
    Z=seg(voltas)
    W=1
    Y=0
    while X<len(voltas) and voltas[X][Y]!=Z:
        while Y<len(voltas[0]):
            if Z==voltas[X][Y]:
                W=W+Y
            Y=Y+1
        X=X+1
        Y=0
    return (corredor(voltas),seg(voltas),W)
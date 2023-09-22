from math import floor
def qtsComfarinha(far):
    numBolos = far/2
    return floor(numBolos)

def qtsComovo(ovo):
    numBolos = ovo/3
    return floor(numBolos)

def qtsComleite(lei):
    numBolos = lei/5
    return floor(numBolos)
    
def bolos(far, ovo, lei):
    boloF = qtsComfarinha(far)
    boloO = qtsComovo(ovo)
    boloL = qtsComleite(lei)

    return min(boloL, boloO, boloF)
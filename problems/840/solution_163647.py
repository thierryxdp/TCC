def qtsComfarinha(far):
    numBolos = far/2
    return round(numBolos, 0)

def qtsComovo(ovo):
    numBolos = ovo/3
    return round(numBolos, 0)

def qtsComleite(lei):
    numBolos = lei/5
    return round(numBolos, 0)
    
def bolos(far, ovo, lei):
    boloF = qtsComfarinha(far)
    boloO = qtsComovo(ovo)
    boloL = qtsComleite(lei)

    return min(boloL, boloO, boloF)
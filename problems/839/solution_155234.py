def carros (p,cv):
    #calculo do numero de carros#
    if p <= 5:
        return 1 
    elif p > 5:
        return int (p/cv)+1
    else:
        return 0
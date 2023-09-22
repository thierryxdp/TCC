def carros (p):
    #calculo do numero de carros#
    if p <= 5:
        return 1
    elif p>=5:
        return int (p/cv) +1
    else:
        return int (p/5)+1
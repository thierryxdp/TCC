def carros (p,cv):
    #calculo do numero de carros#
    if (p):
        return int (p/5)
    
    elif (p<=5):
        return 1 
    
    else:
        return int (p/cv)
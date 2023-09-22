def carros (p,cv):
    #calculo do numero de carros#
    if (p<=5):
        return 1 
    elif (cv=0):
        return int (p/5)
    
    else:
        return int (p/cv)
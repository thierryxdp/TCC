def filtra_pares(tupla):
    x = tupla[0]
    y = tupla[1]
    z = tupla[2]
    w = tupla[3]
    
    par1 = (x%2 == 0)
    par2 = (y%2 == 0)
    par3 = (z%2 == 0)
    par4 = (w%2 == 0)
    
    if (par1 == True):
        tupla[0] = x
    elif (par2 == True):
        tupla[1] = y
    elif (par3 == True):
        tupla[2] = z
    elif (par4 == True):
        tupla[3] = w
    else:
        return tupla[0], tupla[1], tupla[2], tupla[3]
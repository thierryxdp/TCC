def filtra_pares(tupla):
    x = tupla[0]
    y = tupla[1]
    z = tupla[2]
    w = tupla[3]
    
    par1 = (x%2 == 0)
    par2 = (y%2 == 0)
    par3 = (z%2 == 0)
    par4 = (w%2 == 0)
    
    if (x%2 == 0):
        tupla[0] = x
    elif (y%2 == 0):
        tupla[1] = y
    elif (z%2 == 0):
        tupla[2] = z
    elif (w%2 == 0):
        tupla[3] = w
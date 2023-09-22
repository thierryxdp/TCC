def filtra_pares(tupla):
    x = tupla[0]
    y = tupla[1]
    z = tupla[2]
    w = tupla[3]
    
    par1 = (x%2 == 0)
    par2 = (y%2 == 0)
    par3 = (z%2 == 0)
    par4 = (w%2 == 0)
    
    if (par1 == True and par2 == True and par3 == True and par4 == True):
        return tupla[0], tupla[1], tupla[2], tupla[3]
    else:
        return ()
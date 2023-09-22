def filtra_pares(tupla):
    x = tupla[0]
    y = tupla[1]
    z = tupla[2]
    w = tupla[3]
    
    par1 = (x%2 == 0)
    par2 = (y%2 == 0)
    par3 = (z%2 == 0)
    par4 = (w%2 == 0)

    
    return (par1, par2, par3, par4)
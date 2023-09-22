def filtra_pares(tupla):
    '''
    Função que recebe uma tupla de quatro elementos inteiros e iremos filtrá-la,
    ou seja, iremos retornar apenas os seus números pares na mesma ordem em que se
    encontravam no início.
    Param tupla: int
    Return: int
    '''
    x = tupla[0]
    y = tupla[1]
    z = tupla[2]
    w = tupla[3]
    
    par1 = (x%2 == 0)
    par2 = (y%2 == 0)
    par3 = (z%2 == 0)
    par4 = (w%2 == 0)
    
    if (par1 == True and par2 == True and par3 == True and par4 == True):
        return (tupla[0], tupla[1], tupla[2], tupla[3])
    elif (par1 == True and par2 == True and par3 == True):
        return (tupla[0], tupla[1], tupla[2])
    elif (par1 == True and par2 == True and par4 == True):
        return (tupla[0], tupla[1], tupla[3])
    elif (par1 == True and par3 == True and par4 == True):
        return (tupla[0], tupla[2], tupla[3])
    elif (par2 == True and par3 == True and par4 == True):
        return (tupla[1], tupla[2], tupla[3])
    elif (par1 == True and par2 == True):
        return (tupla[0], tupla[1])
    elif (par1 == True and par3 == True):
        return (tupla[0], tupla[2])
    elif (par1 == True and par4 == True):
        return (tupla[0], tupla[3])
    elif (par3 == True and par4 == True):
        return (tupla[2], tupla[3])
    elif (par2 == True and par3 == True):
        return (tupla[1], tupla[2])
    elif (par2 == True and par4 == True):
        return (tupla[1], tupla[3])
    elif (par1 == True):
        return (tupla[0], )
    elif (par2 == True):
        return (tupla[1], )
    elif (par3 == True):
        return (tupla[2], )
    elif (par4 == True):
        return (tupla[3], )
    else:
        return ()
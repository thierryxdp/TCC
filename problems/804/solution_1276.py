def filtra_pares(x):
    '''dado uma tupla com quatro numeros inteiros, retorna uma nova tupla
    apenas com os elementos pares da tupla dada como entrada;
    tuple -> tuple'''
    
    x1,x2,x3,x4 = x   
    par1 = x1%2 == 0
    par2 = x2%2 == 0
    par3 = x3%2 == 0
    par4 = x4%2 == 0

    if par1 and par2 and par3 and par4:
        return (x1,x2,x3,x4)
    elif par1 and par2 and par3:
        return (x1,x2,x3)
    elif par1 and par2 and par4:
        return (x1,x2,x4)
    elif par1 and par2:
        return(x1,x2)
    elif par1 and par3 and par4:
        return (x1,x3,x4)
    elif par1 and par4:
        return (x1,x4)
    elif par1 and par3:
        return (x1,x3)
    elif par2 and par3 and par4:
        return (x2,x3,x4)
    elif par2 and par3:
        return (x2,x3)
    elif par2 and par4:
        return (x2,x4)
    elif par3 and par4:
        return (x3,x4)
    elif par1:
        return (x1)
    elif par2:
        return (x2)
    elif par3:
        return (x3)
    elif par4:
        return (x4,)
    else:
        return ()
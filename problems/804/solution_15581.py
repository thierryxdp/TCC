#Start your python function here
def filtragem(F):
    '''
    Função que recebe uma tupla com quatro valores int e realiza uma filtragem deles.
    Retornando neste caso os seus números pares na mesma ordem em que se encontravam no começo.
    int-->int
    '''
    a = F[0]
    b = F[1]
    c = F[2]
    d = F[3]
    
    par1 = (a%2 == 0)
    par2 = (b%2 == 0)
    par3 = (c%2 == 0)
    par4 = (d%2 == 0)
    
    if (par1 == True and par2 == True and par3 == True and par4 == True):
        return (F[0], F[1], F[2], F[3])
    
    elif (par1 == True and par2 == True and par3 == True):
        return (F[0], F[1],F[2])
    
    elif (par1 == True and par2 == True and par4 == True):
        return (F[0], F[1], F[3])
    
    elif (par1 == True and par3 == True and par4 == True):
        return (F[0], F[2], F[3])
    
    elif (par2 == True and par3 == True and par4 == True):
        return (F[0], F[2], F[3])
    
    elif (par1 == True and par2 == True):
        return (F[0], F[1])
    
    elif (par1 == True and par3 == True):
        return (F[0], F[2])
    
    elif (par1 == True and par4 == True):
        return (F[0], F[3])
    
    elif (par3 == True and par4 == True):
        return (F[0], F[3])
    
    elif (par2 == True and par3 == True):
        return (F[0], F[2])
    
    elif (par1 == True):
        return (F[0], )
    
    elif (par2 == True):
        return (F[1], )
    
    elif (par3 == True):
        return (F[2], )
    
    elif (par4 == True):
        return (tupla[3], )
    
    else:
        return ()
def filtra_pares(numeros):
    """Retorna uma tupla contendo os elementos
       pares da tupla original. Insira uma tupla
       com 4 elementos inteiros;tuple->tuple"""
    par1=numeros[0]%2==0
    par2=numeros[1]%2==0
    par3=numeros[2]%2==0
    par4=numeros[3]%2==0
    if par1==True:
        if par2==True:
            if par3==True:
                if par4==True:
                    return numeros
    if par1==True and par2==True:
        return numeros[0:2]
    if par1==True and par3==True:
        return numeros[0:4:-2]
    if par1==True and par4==True:
        return numeros[0::-3]
    if par2==True and par3==True:
        return numeros[1:3]
    if par2==True and par4==True:
        return numeros[1::-2]
    if par3==True and par4==True:
        return numeros[2:]
    else:
        str(())
def filtra_pares(numeros):
    """Retorna uma tupla contendo os elementos
       pares da tupla original. Insira uma tupla
       com 4 elementos inteiros; tuple->tuple"""
    par0=numeros[0]%2==0
    par1=numeros[1]%2==0
    par2=numeros[2]%2==0
    par3=numeros[3]%2==0
    if par0==True and par1==True and par2==True and par3==True:
        return tuple(numeros)
    if par0==True and par1==False and par2==False and par3==False:
        return numeros[0],
    if par0==False and par1==True and par2==False and par3==False:
        return numeros[1],
    if par0==False and par1==False and par2==True and par3==False:
        return numeros[2],
    if par0==False and par1==False and par2==False and par3==True:
        return numeros[3],
    if par0==True and par1==True and par2==False and par3==False:
        return tuple(numeros[0:2])
    if par0==True and par2==True and par1==False and par3==False:
        return numeros[0],numeros[2]
    if par0==True and par3==True and par1==False and par2==False:
        return numeros[0],numeros[3]
    if par0==True and par1==True and par2==True and par3==False:
        return numeros[0],numeros[1],numeros[2]
    if par0==True and par1==True and par3==True and par2==False:
        return numeros[0],numeros[1],numeros[3]
    if par0==True and par2==True and par3==True and par1==False:
        return numeros[0],numeros[2],numeros[3]
    if par1==True and par2==True and par0==False and par3==False:
        return numeros[1],numeros[2]
    if par1==True and par3==True and par0==False and par2==False:
        return numeros[1],numeros[3]
    if par2==True and par3==True and par0==False and par1==False:
        return numeros[2],numeros[3]
    if par1==True and par2==True and par3==True and par0==False:
        return numeros[1],numeros[2],numeros[3]
    else:
        return str(())
def filtra_pares(tupla):
    '''Função que recebe uma tupla, digitada pelo
    usuário,de quatro elementos. A função, então,
    retorna a filtragem dos pares dos elementos, isto é,
    retornará apenas os elementos pares, por meio 
    de uma nova tupla.'''
    if(tupla[0]%2==0):
        par0=(tupla[0],)
    else:
        par0=()
    
    if(tupla[1]%2==0):
        par1=(tupla[1],)
    else:
        par1=()
    
    if(tupla[2]%2==0):
        par2=(tupla[2],)
    else:
        par2=()
    
    if(tupla[3]%2==0):
        par3=(tupla[3],)
    else:
        par3=()
    return (par0+par1+par2+par3)
def faltante(L):
    '''
    '''
    
    lista=[]
    proximo=0
    while proximo<(len(L)-1):
        if L[proximo]==(L[proximo+1]-1):
            lista= lista+[]
        else:
            lista=lista+[L[proximo+1]]
        proximo=proximo+1
    return lista
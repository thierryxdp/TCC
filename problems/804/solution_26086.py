def filtra_pares(tupla):
    '''recebe uma tupla com 4 elementos e retorna os elementos pares dela'''
    conj_pares = ()
    if(tupla[0] %2 == 0):
        conj_pares += (tupla[0],)
    if(tupla[1] %2 == 0):
        conj_pares += (tupla[1],)
    if(tupla[2] %2 == 0):
        conj_pares += (tupla[2],)
    if(tupla[3] %2 == 0):
        conj_pares += (tupla[3],)
    
    return conj_pares
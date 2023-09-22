def filtra_pares(tup):
    '''funçao que recebe uma tupla com quatro inteiros e retoma uma tupla apenas os elementos pares. tupla->tupla'''
    pares = ()
    if(tup[0]%2 == 0):
        pares = pares + (tup[0],)
    if(tup[1]%2 == 0):
        pares = pares + (tup[1],)    
    if(tup[2]%2 == 0):
        pares = pares + (tup[2],)    
    if(tup[3]%2 == 0):
        pares = pares + (tup[3],)
    return pares
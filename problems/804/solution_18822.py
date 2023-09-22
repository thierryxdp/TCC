def filtra_pares (elementos):
    '''
    recebe quatro elementos e retorna uma nova tupla
    contendo apenas os elementos pares
    '''
    elem1, elem2, elem3, elem4= elementos
    pares= tuple()
    
    if elem1%2==0:
        pares+= (elem1,)
    
    if elem2%2==0:
        pares+= (elem2,)
        
    if elem3%2==0:
        pares+= (elem3,)
        
    if elem4%2==0:
        pares+= (elem4,)
        
    return pares
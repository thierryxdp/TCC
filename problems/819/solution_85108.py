def filtraMultiplos(lista,N):
    ''' 
    Recebe uma lista contendo int e N
    Retorna uma lista de elementos que são divisíveis por n
    
    '''
    elementos=[]
    for x in lista:
        if x % N == 0:
            elementos.append(x)
    return elementos
def filtraMultiplos(x,y):
    '''A função retorna os números da lista x que são
    divisíveis por y
    lista, int/float -> lista'''
    
    i = 0
    u = []
    
    while len(x)>i:
        if x[i]%y == 0:
            list.append(u, x[i])
        i = i + 1
        
    return u
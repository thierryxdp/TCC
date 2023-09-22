def filtra_pares(x):
    '''Verifica quais números são pares e é retornado em uma nova tupla
    tupla->tupla'''
    
    i = 0
    y = ()
    
    while i<len(x):
        if x[i]%2==0:
            y = y + x[i]
        i = i + 1
    return y
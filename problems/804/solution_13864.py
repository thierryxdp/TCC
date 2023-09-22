def filtra_pares(a,b,c,d):
    '''
    função recebe uma tupla com quaro inteiros e retorne uma nova
    contendo apenas os elementos pares da tupla original;
    tuple -> tuple
    '''
    
    if (a%2 == 0):
        return (a)
        
    elif (b%2 == 0):
        return (b)
        
    elif (c%2 == 0):
        return (c)
        
    elif (d%2 == 0):
        return (d)
        
    elif (a%2 == 0) and (b%2 == 0):
        return (a, b)

    elif (a%2 == 0) and (b%2 == 0) and (c%2 == 0):
        return (a, b, c)
        
    elif (a%2 == 0) and (b%2 == 0) and (c%2 == 0) and (d%2 == 0):
        return (a, b, c, d)
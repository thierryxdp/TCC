def filtra_pares(abcd):
    '''
    função recebe uma tupla com quaro inteiros e retorne uma nova
    contendo apenas os elementos pares da tupla original;
    tuple -> tuple
    '''
    a = abcd[0]
    b = abcd[1]
    c = abcd[2]
    d = abcd[3]
    
    if (a%2 == 0) and (b%2 == 0) and (c%2 == 0) and (d%2 == 0):
        return ((a, b, c, d))
        
    elif (a%2 == 0) and (b%2 == 0):
        return ((a, b))
    
    elif (a%2 == 0) and (d%2 == 0):
        return ((a, d))
    
    elif (a%2 == 0) and (c%2 == 0) and (d%2 == 0):
        return ((a,c,d))

    elif (a%2 == 0) and (b%2 == 0) and (c%2 == 0):
        return ((a, b, c))
    
        
      
    elif (b%2 == 0) and (c%2 == 0) and (d%2 == 0):
        return ((b,c,d))
    
    elif (a%2 == 0):
        return ((a,))
        
    elif (b%2 == 0):
        return ((b,))
        
    elif (c%2 == 0):
        return ((c,))
        
    elif (d%2 == 0):
        return ((d,))    
    
    
    else: 
        return ()
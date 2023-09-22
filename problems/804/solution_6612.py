def filtra_pares (t):
    '''função que retorna uma tupla nova que contém apenas os elementos
    pares da tupla original, ou seja, que filtre a tupla (t) de entrada e
    retorne uma tupla com seus pares;
    tupla->tupla'''
    a = t[0]
    b = t[1]
    c = t[2]
    d = t[3]
    
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return t
        if a%2==0 and c%2==0:
            return (a,c)
        if b%2==0 and d%2==0:
            return (b,d)
        if a%2==0 and b%2==0:
            return (a,b)
        if a%2==0 and d%2==0:
            return (a,d)
        if a%2==0 and c%2==0 and d%2==0:
            return (a,c,d)
        if a%2==0 and b%2==0 and d%2==0:
            return (a,b,d)
        if a%2==0 and b%2==0 and c%2==0:
            return (a,b,c)
        

        
    else:
        return ()
def filtra_pares (t):
    '''função que retorna uma tupla nova que contém apenas os elementos
    pares da tupla original, ou seja, que filtre a tupla (t) de entrada e
    retorne uma tupla com seus pares;
    tupla->tupla'''
    a = t[0]
    b = t[1]
    c = t[2]
    d = t[3]
    
    if a%2==0:
        if b%2==0:
            if c%2==0:
                if d%2==0:
                    return t
                else:
                    return a,b,c
    else:
        return ()
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
    else:
        if a%2==0 and c%2==0 and d%2==0 and not(b%2==0):
            return (a,c,d)
        else:
            if a%2==0 and b%2==0 and d%2==0 and not(c%2==0):
                return (a,b,d)
            else:
                if a%2==0 and b%2==0 and c%2==0 and not(d%2==0):
                    return (a,b,c)
                else:
                    if b%2==0 and c%2==0 and d%2==0 and not(a%2==0):
                        return (b,c,d)
                    else:
                        if a%2==0 and c%2==0 and not(b%2==0 and d%2==0):
                            return (a,c)
                        else:
                            if b%2==0 and d%2==0 and not(a%2==0 and c%2==0):
                                return (b,d)                            
                            else:
                                if b%2==0 and c%2==0 and not(a%2==0 and d%2==0):
                                    return (b,c)
                            else:
                                return ()
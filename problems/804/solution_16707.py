def filtra_pares(a,b,c,d):
    
    if (a%2==0):
        tupla = (a,)
    else:
        tupla = ()
    
    if (b%2==0):
        tupla = tupla +(b,)
    else:
        tupla = tupla
        
    if (c%2==0):
        tupla = tupla + (c,)
    else:
        tupla = tupla
        
    if (d%2==0):
        tupla = tupla + (d,)
    else:
        tupla = tupla
    
    return tupla
def filtra_pares([a,b,c,d]):
    
    if (a%2==0):
        tupla = (a,)
    elif(b%2==0):
        tupla = tupla +(b,)
    elif (c%2==0):
        tupla = tupla +(c,)
    elif (d%2==0):
        tupla = tupla + (d,)
    else:
        tupla = ()
    
    return tupla
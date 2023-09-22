def filtra_pares(a,b,c,d):
    
    if (a%2==0) and (b%2==0) and (c%2==0) and (d%2==0):
        tupla = (a,b,c,d)
    elif (a%2==0) and (b%2==0) and (c%2==0) and (d%2!=0):
        tupla = (a,b,c)
    elif (a%2==0) and (b%2==0) and (c%2!=0) and (d%2==0):
        tupla = (a,b,d)
    elif (a%2==0) and (b%2!=0) and (c%2==0) and (d%2==0):
        tupla = (a,c,d)
    elif (a%2!=0) and (b%2==0) and (c%2==0) and (d%2==0):
        tupla = (b,c,d)
    elif (a%2!=0) and (b%2!=0) and (c%2==0) and (d%2==0):
        tupla = (c,d)
    elif (a%2==0) and (b%2!=0) and (c%2!=0) and (d%2==0):
        tupla = (a,d)
    elif (a%2==0) and (b%2==0) and (c%2!=0) and (d%2!=0):
        tupla = (a,b)
    elif (a%2!=0) and (b%2==0) and (c%2!=0) and (d%2==0):
        tupla = (b,d)
    elif (a%2!=0) and (b%2==0) and (c%2==0) and (d%2!=0):
        tupla = (b,c)
    elif (a%2==0) and (b%2!=0) and (c%2==0) and (d%2!=0):
        tupla = (a,c)
    elif (a%2==0) and (b%2!=0) and (c%2!=0) and (d%2!=0):
        tupla = (a,)
    elif (a%2!=0) and (b%2==0) and (c%2!=0) and (d%2!=0):
        tupla = (b,)
    elif (a%2!=0) and (b%2!=0) and (c%2==0) and (d%2!=0):
        tupla = (c,)
    elif (a%2!=0) and (b%2!=0) and (c%2!=0) and (d%2==0):
        tupla = (d,)
        
    return tupla
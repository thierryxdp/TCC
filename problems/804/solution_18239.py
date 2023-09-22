def filtra_pares(tupla):
    a=tupla[0]
    b=tupla[1]
    c=tupla[2]
    d=tupla[3]

    if (a%2==0):
        a=tuple(a,)
    if (b%2==0):
        b=tuple(b,)
    if (c%2==0): 
        c=tuple(c,)
    if (d%2==0):
        d=tuple(d,)
        
        return a+b+c+d
    
    
    else:
        return ()
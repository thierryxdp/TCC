def filtra_pares(tupla):
    a=tupla[0]
    b=tupla[1]
    c=tupla[2]
    d=tupla[3]

    if a%2==0:
        a=str(a)
    if b%2==0:
        b=str(b)
    if c%2==0: 
        c=str(c)
    if d%2==0:
        d=str(d)
        
        a1=str(a)
        b1=str(b)
        c1=str(c)
        d1=str(d)
        
        return (a1,b1,c1,d1)
    
    
    else:
        return ()
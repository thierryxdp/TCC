def posLetra(f,letra,i):
    c=1
    ii=0
    if i>f.count(letra):
        return -1
    while letra in f:
        if f[ii]==letra:
            if c==i:
                return ii
            c+=1
            
        ii+=1
    
    else:
        return -1
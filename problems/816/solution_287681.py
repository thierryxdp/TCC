def maiores(l,n):
    d=()
    for numeros in l:
        if numeros>n:
            d=d+(numeros,)            
    return d
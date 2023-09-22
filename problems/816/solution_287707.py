def maiores(l,n):
    d=[]
    for numeros in l:
        if numeros>n:
            d+=[numeros]            
    i=sorted(d)
    return i
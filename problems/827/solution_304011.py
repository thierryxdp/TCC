def qtd_divisores(n):
    d=0
    for e in range(1,n+1):
        if n%e==0:
            d+=1
    return d
def qtd_divisores(n):
    d=1
    i=0
    while i<n:
        if n%d==0:
            d=d+1
    if n<=0:
            d=0
        i=i+1
    return d
def qtd_divisores(n):
    d=0
    i=0
    if n<=0:
        return 0       
    while i<n:
        if n%d+1==0:
            d=d+1
        i=i+1
    return d
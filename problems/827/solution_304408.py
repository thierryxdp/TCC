def qtd_divisores(n):
    d=1
    if n<0:
        return 0
    for i in range(2,n):
        if n%1==0:
            d=d+1
    return d+1
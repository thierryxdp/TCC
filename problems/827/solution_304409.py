def qtd_divisores(n):
    d=1
    if n<0:
        return 0
    for i in range(2,n):
        if n%i==0:
            d=d+1
    return d+1
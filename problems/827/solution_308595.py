def qtd_divisores(n):
    d=0
    for i in range(1, n//2+1):
        if n%i==0:
            d=i
    return n
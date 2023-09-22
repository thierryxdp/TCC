def qtd_divisores(n):
    i=1
    zero=0
    while i<=n:
        if n%i==0:
            zero=zero+1
            i=i+1
        else:
            i=i+1
    return zero
def qtd_divisores(n):
    qtd = 1
    total = 0
    for i in range(1,n+1):
        if  n% i==0:
            total = total + qtd
            qtd=qtd*i
    return total
def qtd_divisores(n):
    qtd = 1
    total = 0
    for i in range(1,n+1):
        if  n% i==0:
            qtd = qtd*i
            total= total + qtd
    return total
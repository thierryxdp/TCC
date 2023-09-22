def qtd_divisores(n):
    total = 0
    qtd = 1
    for i in range(1,n+1):
        total = total + qtd
        qtd = qtd*i
    return total
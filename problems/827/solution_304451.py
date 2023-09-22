def qtd_divisores(n):
    qtdDiv = 0
    for i in range(1,n+1):
        if n%i == 0:
            qtdDiv += 1
    return qtdDiv
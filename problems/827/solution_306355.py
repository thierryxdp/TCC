def qtd_divisores(n):
    qtd = 0
    for i in range(n):
        if (n%(i+1)) == 0:
            qtd = qtd + 1
    return qtd
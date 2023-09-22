def qtd_divisores(n):
    total = 0
    qtd = 1
    for i in range(n+ 1):
        total = total + qtd
        qtd = qtd*i
    return total
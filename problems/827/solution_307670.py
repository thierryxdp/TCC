def qtd_divisores(a):
    qtd = 0
    for e in range(a):
        if (a//e)*e == a:
            qtd = qtd + 1
    return qtd
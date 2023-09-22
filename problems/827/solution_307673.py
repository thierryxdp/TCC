def qtd_divisores(a):
    qtd = 0
    for e in range(a):
        if (a//(e+1))*(e+1) == a:
            qtd = qtd + 1
    return qtd
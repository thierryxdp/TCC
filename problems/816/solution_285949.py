def maiores(lista, x):
    y = [i for i in lista if i > x]
    acao1 = y.sort(reverse=False)
    return y
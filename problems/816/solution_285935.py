def maiores(lista, x):
    acao1 = lista.sorted(reverse=False, key=lista[0]>x)
    return acao1
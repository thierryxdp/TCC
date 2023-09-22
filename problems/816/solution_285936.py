def maiores(lista, x):
    acao1 = lista.sort(reverse=False, key=lista[0]>x)
    return acao1
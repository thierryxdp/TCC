def maiores(lista, x):
    acao1 = lista.sort(reverse=False, key=x>0)
    return lista
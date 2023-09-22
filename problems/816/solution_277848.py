def maiores(lista, n):
    list(lista)
    lista = list(lista.insert(0, n))
    lista = sorted(lista)
    indice = find(n, lista)
    qntdmaiores = len(lista) - (indice + 1)
    return list(qntdmaiores)
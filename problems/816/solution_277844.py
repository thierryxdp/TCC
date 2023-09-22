def maiores(lista, n):
    list(lista)
    list(lista = lista.insert(0, n))
    lista = sorted(lista)
    indice = find(n, lista)
    qntdmaiores = len(lista) - (indice + 1)
    return list(qntdmaiores)
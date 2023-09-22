def maiores(lista, n):
    list(lista)
    lista = lista.insert(0, n)
    lista = sorted(list(lista))
    indice = find(n, lista)
    qntdmaiores = len(lista) - (indice + 1)
    return list(qntdmaiores)
def maiores(lista,n):
    lista.append(n)
    lista1 = lista[:]
    lista1.sort()
    posicao = lista1.index(n) + 1
    lista_ordem1 = lista1[posicao:]
    return lista_ordem1
def maiores(lista, n):
    list.sort(lista)
    list.reverse(lista)
    lista1 = []
    posicao = 0
    while lista[posicao] > n:
        lista1.append(lista[posicao])
        posicao = posicao + 1
    return lista1.reverse
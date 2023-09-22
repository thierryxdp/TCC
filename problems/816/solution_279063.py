def maiores(lista, n):
    list.sort(lista)
    list.reverse(lista)
    lista1 = []
    posicao = 0
    lista2 = list.reverse(lista1)
    while lista[posicao] > n:
        lista1.append(lista[posicao])
        posicao = posicao + 1
    return lista2
def maiores(lista):
    lista1 = lista[0]
    list.sort(lista1)
    list.reverse(lista1)
    lista2 = []
    posicao = 0
    while lista1[posicao] > lista[1]:
        lista2.append(lista1[posicao])
        posicao = posicao + 1
    return list.reverse(lista2)
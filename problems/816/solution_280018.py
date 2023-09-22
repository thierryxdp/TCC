def maiores(lista1, n):
    list.insert(lista1, 0, n)
    list.sort(lista1)
    indice = list.index(lista1, n) + 1
    frase_nova = lista1[indice:]
    return frase_nova
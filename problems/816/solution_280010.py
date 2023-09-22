def maiores(lista1, n):
    list.insert(lista1, n, 0)
    list.sort(lista1)
    indice = str.index(lista1, [n])
    frase_nova = lista1[indice:]
    return frase_nova
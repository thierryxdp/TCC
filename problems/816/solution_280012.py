def maiores(lista1, n):
    list.insert(lista1, n, 0)
    list.sort(lista1)
    indice = list.index(lista1, n) + 1
    frase[indice:] = frase_nova
    return frase_nova
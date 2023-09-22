def maiores(lista, n):
    """Retorna uma nova lista contendo todos os numeros da lista original
    maiores que n, dados: lista e n(um numero inteiro)"""

    list(lista)
    lista.append(n)
    listaO=sorted(lista)
    indiceN=listaO.index(n)

    if n not in listaO:
        lista.append(n)

    return listaO[indiceN+1:]
def maiores(lista, n):
    """Funcao retorna uma lista com os elementos da lista original dada:
    lista que sao maiores que o numero dado: n """

    if n in lista:
        lista.sort()
        posicao = lista.index(n)
        lista_final = lista[posicao+1:]
    else:
        lista.append(n)
        lista.sort()
        posicao = lista.index(n)
        lista_final = lista[posicao+1:]

    return lista_final
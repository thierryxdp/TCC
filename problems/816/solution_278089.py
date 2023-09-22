def maiores(lista_numeros, n):
    """
    Dada uma lista de números e um número n, gera uma nova lista contendo os números maiores do que n
    e os inserem dentro dessa nova lista.
    :param lista_numeros:
    :param n:
    :return:
    """
    listaInicial = lista_numeros
    novaLista = []
    maiorDaLista = max(listaInicial)
    if n < maiorDaLista:
        novaLista.append(listaInicial[n:maiorDaLista])

    return novaLista
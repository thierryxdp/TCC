def maiores(lista_numeros, n):
    """
    Dada uma lista de números e um número n, gera uma nova lista contendo os números maiores do que n
    e os inserem dentro dessa nova lista.
    :param lista_numeros:
    :param n:
    :return:
    """
    lista = lista_numeros
    maiorDaLista = max(lista)
    if n < maiorDaLista:
        return lista[n:maiorDaLista]
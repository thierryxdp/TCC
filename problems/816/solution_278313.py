def maiores(lista,n):
    """Dada uma lista de números inteiros e um valor 'n',
    retorna uma nova lista com os valores da lista anterior
    maiores que o valor em 'n'."""
    lista.insert(n,n)
    lista.sort()
    return lista[n:]
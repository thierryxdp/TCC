def filtra_mult_n (lista, n):
    """Filtra os números da lista que são multiplos de n
    list, int -> list"""
    lista1 = [ ]
    proximo = 0
    while proximo<len(lista):
        if lista[proximo] % n == 0:
            lista1 = lista1 + [lista[proximo]]
        proximo = proximo + 1
    return lista1
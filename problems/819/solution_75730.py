def filtraMultiplos(lista, n):
    """retorna uma lista contendo todos os elementos
    da lista original que forem divisiveis por um numero n dado """
    lista1 = []
    for i in lista:
        if (i % n == 0):
            lista1.append(i)
    return lista1
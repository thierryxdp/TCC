def filtraMultiplos (lista, n):
    """dada uma lista e um numero n, função retorna outra lista contendo 
    todos os elementos da lista original divisiveis por n. lista -> lista """

    proximo = 0
    multiplos = []
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            multiplos = multiplos + [lista[proximo]]
        proximo = proximo + 1
    return multiplos
def filtraMultiplos(lista, n):
    """Este código filtra os multiplos de um número n, dentre
    a lista inserida.
    Recebe: list, int
    Retorna: list"""
    multiplos = []
    proximo = 0
    while proximo <len(lista):
        if lista[proximo]%n ==0:
            list.append(multiplos, lista[proximo])
        proximo = proximo + 1
    return multiplos
def filtraMultiplos(lista, n):
    """
    Função que recebe uma lista e um número de entrada e retorna uma outra lista com contendo todos os elementos da lista original que forem divisíveis por n
    list, int -> list
"""
    nlista = lista[:]
    multiplos = []
    prox = 0

    while prox < len(nlista):
        if nlista[prox]%n == 0:
            multiplos +=(lista[prox],)
        prox += 1
    return multiplos
def filtraMultiplos(lista, n):
    """Função que dado uma lista(lista e um número(n) retorna outra lista
    contento todos os divisíveis por n.
    list, float -> list"""

    indice = 0
    multiplos = []
    while indice < len(lista):
        if lista[indice]%n == 0:
            multiplos[len(multiplos):len(multiplos)] = [lista[indice]]

    	i += 1

    return multiplos
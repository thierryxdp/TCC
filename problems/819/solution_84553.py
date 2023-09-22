def filtraMultiplos (lista, n):
    """filtra os numeros de uma lista de entrada que sao divisiveis por um numero n de entrada
    list, int -> list"""
    multiplos = []
    for x in lista:
        if x % n == 0:
            multiplos.append(numero)
    return multiplos
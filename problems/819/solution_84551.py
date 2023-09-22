def filtraMultiplos (lista, n):
    """filtra os numeros de uma lista de entrada que sao divisiveis por um numero n de entrada
    list, int -> list"""
    multiplos = []
    for numero in lista:
        if numero // n == 0:
            multiplos.append(numero)
    return multiplos
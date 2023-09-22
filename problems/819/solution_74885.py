"""Recebe uma lista de números e um int n e retorna uma nova lista somente
com os números divisíveis por n
list -> list"""

def filtraMultiplos(lista, n):
    multiplos = []
    i = 0
    while i < len(lista):
        if lista[i] % n == 0:
            multiplos.append(lista[i])
		i = i + 1
    return multiplos
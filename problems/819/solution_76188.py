def filtraMultiplos(lista, n):
    """função que filtra os múltiplos de um número n presentes na lista
    list, int -> list"""
    indice = 0
    multiplos = []
    while indice < len(lista):
        if lista[indice] % n == 0:
            list.append(multiplos,lista[indice])
        indice += 1
    return multiplos
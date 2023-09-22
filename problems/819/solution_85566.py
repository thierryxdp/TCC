def filtraMultiplos(lista, n):
    """função que recebe lista e retorna lista com números múltiplos do número n
    list, int--> list"""
    multiplos = []
    contador = 0
    while contador < len(lista):
        if lista[contador] % n == 0:
            multiplos.insert(contador, lista[contador])
            contador = contador +1
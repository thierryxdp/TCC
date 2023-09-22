def filtraMultiplos(lista:list, n:int) -> list:
    '''Recebe uma lista de números aleatórios e um número n, e retorna uma
    nova lista contendo apenas os múltiplos do número n'''
    i = 0
    multiplos = []
    while i < len(lista):
        if lista[i] % n == 0:
            multiplos.append(lista[i])
        i = i+1
    return multiplos
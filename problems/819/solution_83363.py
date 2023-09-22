def filtraMultiplos(lista, n):
    '''Retorna os números da lista que são múltiplos de n
    	list, int -> list'''
    i = 0
    multiplos = []
    while i < len(lista):
        if lista[i]%n == 0:
            multiplos.append(lista[i])
        i = i + 1
    return multiplos
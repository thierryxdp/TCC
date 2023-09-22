def filtraMultiplos(lista, n):
    '''Retorna os numeros da lista multiplos de n
    list, int -> list.'''
    multiplos = []
    i = 0
    while i < len(lista):
        if lista[i] % n == 0:
       	    multiplos = multiplos + lista[i]
    	i = i + 1
    return multiplos
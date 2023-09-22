def filtraMultiplos(lista, n):
    '''função que retorna uma lista de números múltiplos de um número n, a partir de uma lista de números dada; list, int -> list'''
    
    i = 0
    numero = lista[indice]
    multiplos = []
    
    while i < len(lista):
        if numero%n != 0:
            lista.remove(indice)
            return multiplos
        i = i+1
    return multiplos
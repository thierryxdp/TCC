def filtraMultiplos(lista,n):
    '''função que, dada uma lista e um número (n), filtra os múltiplos desse
    número e os retorna em uma lista; list, float -> list'''
    multiplos = []
    i = 0
    while i < len(lista):
        if lista[i] % n == 0:
            multiplos = multiplos + [lista[i],]
        i = i + 1
    return multiplos
def filtraMultiplos(lista,n):
    '''função que filtra elementos de uma lista retornando outra lista com os múltiplos
    de n. list->list'''
    multiplos = []
    elemento = 0
    while elemento <len(lista):
        if lista[elemento]%n == 0:
            multiplos = multiplos + [lista[elemento],]
        elemento = elemento + 1
    return multiplos
def filtra_multiplos(lista,n):
    '''Recebe uma lista de númer o e um número n e retorna uma
    lista com os números da lista orginal que forem divisíveis
    por n; list(int), int -> list(int)'''
    i = 0
    multiplos = ['']
    while i < len(lista):
        if lista[i] % n == 0:
            multiplos = multiplos + [lista[i]]
        i = i+1
    return multiplos
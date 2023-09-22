def filtraMultiplos(lista,n):
    '''Recebe uma lista de números e um número n, e retorna uma lista com todos os números da lista original que eram divisíveis por n;
    list, int -> list'''

    multiplos = []
    i = 0

    while i < len(lista):
        if lista[i] % n == 0:
            multiplos = multiplos + [lista[i],]
        i = i + 1
    return multiplos
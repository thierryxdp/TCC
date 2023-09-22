def filtraMultiplos(lista,n):
    '''Funcao que dada uma lista e um numero "n", retorna uma outra lista
    contendo todos os elementos da lista original divisiveis por n
    list, float -> list'''
    multiplos = []
    i = 0
    while i<len(lista):
        if lista[i]%n == 0:
            multiplos = multiplos + [lista[i]]
        i = i + 1
    return multiplos
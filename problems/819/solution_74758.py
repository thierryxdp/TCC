def filtraMultiplos(lista,n):
    '''A partir de uma lista e um número 'n';
retorna uma nova lista com os elementos da lista original divisiveis por 'n';
list, int => list'''
    i = 0
    multiplos = []
    while i<len(lista):
        if lista[i]%n==0:
            multiplos = multiplos + [lista[i]]
        i = i+1
    return multiplos
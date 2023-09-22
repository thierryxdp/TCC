def filtraMultiplos(lista, n):
    '''Dada uma lista de números e um número 'n', Retornar outra lista contendo todos
    os elementos da lista original que forem divisiveis por 'n';
    list, int -> list'''

    multiplos = []
    i = 0
    
    while i < len(lista):
        if lista[i] % 2 == 0:
            list.append(multiplos, lista[i])
        i += 1

    return multiplos
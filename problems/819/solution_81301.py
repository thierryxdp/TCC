def filtraMultiplos(lista, n):
    '''Funçao que, fornecida uma lista de numeros e um numero n,
    retorna outra lista contendo todos os elementos divisiveis
    por n da lista original
    list, int -> list'''
    i = 0
    multiplos = []
    while i < len(lista):
        if lista[i] % n == 0:
            list.append(multiplos, lista[i])
        i = i + 1
    return multiplos
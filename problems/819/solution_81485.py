def filtraMultiplos (numeros, n):
    '''Retorna todos os numeros divisiveis
    por n, da lista de numeros dada
    list, int --> list'''
    divisiveis = []
    i=0
    while i < len(numeros):
        if int(numeros[i])%n == 0:
            divisiveis += [numeros[i]]
        i += 1
    return divisiveis
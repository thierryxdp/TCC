def filtraMultiplos(lista,n):
    '''Funcao que filtra os multiplos de um numero n, recebendo como entrada
    uma lista de numeros e o numero. Ela dever retornar uma outra lista
    contendo todos os elementos da lista original que forem divisiveis por n'''
    lista1 = ()
    i = 0
    while i < len(lista):
        if int(lista[i])%n == 0:
            lista1 = lista1 + (lista[i],)
        i = i + 1
    return list(lista1)
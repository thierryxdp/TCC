def filtraMultiplos(lista,n):
    '''recebe uma lista de numeros e um numero, retornando outra lista contendo
    todos os elementos da lista original que forem divisiveis por n'''
    divisiveis = []
    proximo = 0

    while proximo <len(lista):
        if lista[proximo]%n == 0:
            divisiveis = divisiveis + (lista[proximo],)
        proximo = proximo + 1
    return divisiveis
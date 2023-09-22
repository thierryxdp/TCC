def filtraMultiplos(lista,n):
    '''Função que recebe uma lista de numeros e um numero, e retorna uma outra lista
contendo todos os elementos da lista original que forem divisiveis por n.
    list,float-->list'''
    multiplos = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            list.append(multiplos,lista[proximo])
        proximo = proximo + 1
    return multiplos
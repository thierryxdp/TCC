def filtraMuliplos(lista,n):
    '''
	função que recebe uma lista e um número e retorna outra lista contendo todos os elementos da lista original que forem divisíveis por n;
    list, int -> list
    '''
    i = 0
    divisiveis = []
    while i < len(lista):
        if lista[i]%n == 0:
            divisiveis = divisiveis + (lista[i],)
        i = i+1
    return divisiveis
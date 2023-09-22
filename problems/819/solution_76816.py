def filtra_multiplos(lista,n):
    
    '''função que recebe uma lista e um número n e retorna uma lista contendo todos os elementos da lista original que forem divisíveis por n.
    list, int -> list'''
    
    lista1 = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            list.append (lista1, lista[proximo])
        proximo = proximo + 1
    return lista1
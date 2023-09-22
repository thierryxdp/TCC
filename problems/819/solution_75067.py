def filtraMultiplos(lista, n):
    '''função que recebe uma lista de números e um elemento n, e retorna os elementos da lista original que são múltiplos
    de n, na ordem original.
    list, int -> list'''
    
    indice = 0
    divisiveis= []
    
    while indice<len(lista):
        if lista[indice]%n==0:
            list.append(divisiveis, lista[indice])
        indice = indice + 1
    return divisiveis
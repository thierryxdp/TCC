def filtraMultiplos(lista, n):
    '''Função que recebe uma lista e um número, e retornará
    uma outra lista contendo todos os elementos da lista
    original que forem divisíveis por esse número.
    list, int -> list'''
    
    lista_final = []
    result = 0
    while result < len(lista):
        if lista[result]%n == 0:
        	lista_final = lista_final + [lista[result],]
        result = result + 1
    return lista_final
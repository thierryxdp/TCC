def maiores(lista, n):
    '''Dada uma lista de numeros inteiros e um numero 
    inteiro n retorna uma lista com os números maiores 
    que n.
    list, int -> list'''
    lista.append(n)
    lista.sort()
    return lista[lista.index(n) + 1:]
def maiores(lista, n):
    '''fução que retorna, a partir de uma lista de números inteiros e um número inteiro n, outra lista porém somente com os números maiores que n da lista principal; list, list'''
    
    lista.sort()
    if lista[0]>n:
        return [lista[0]]
    if lista[1]>n:
        return [lista[0],lista[1]]
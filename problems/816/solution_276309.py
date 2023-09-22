def maiores(lista, n):
    '''fução que retorna, a partir de uma lista de números inteiros e um número inteiro n, outra lista porém somente com os números maiores que n da lista principal; list, list'''
    
    list.sort(lista)
    
    for x in lista:
        if x>n:
        return [i]
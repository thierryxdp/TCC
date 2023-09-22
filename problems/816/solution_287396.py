def maiores (lista, n):
    '''Função que retorna, em ordem crescente, os números de uma lista
    maiores que n
    list -> list'''
    
    if lista <= n:
        return [i for i in lista if i > n]
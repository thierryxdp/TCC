def maiores (lista, n):
    '''Função que retorna, em ordem crescente, os números de uma lista
    maiores que n
    list -> list'''
    ordem_crescente = [lista]
    n_inteiro = [n]
    
    return list.sort(ordem_crescente + n_inteiro)
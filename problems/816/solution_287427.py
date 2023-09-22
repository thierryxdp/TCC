def maiores (lista, n):
    '''Função que retorna, em ordem crescente, os números de uma lista
    maiores que n
    list -> list'''
    lista_retorno = list.sort(lista)
    
    return [i for i in lista if i > n] or [lista_retorno]
def maiores (lista, n):
    '''Função que retorna, em ordem crescente, os números de uma lista
    maiores que n
    list -> list'''
    lista = list.sort(lista)
    
    if n>lista:
        return []
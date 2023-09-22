def maiores (lista, n):
    '''Função que retorna, em ordem crescente, os números de uma 
    lista maiores que n
    list -> list'''
    lista_retorno = list.sort(lista)
    return [i for i in lista if i > n]

def acima_da_media (lista_media):
    lista_ordem = list.sort(lista_media)
    return [i for i in lista if i > n]
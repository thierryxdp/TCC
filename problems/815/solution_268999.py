def insere(lista_numero):
    '''função que dadas uma lista ordenada crescente de números e um numero n, retorna 
       a lista com o número n incluso na posição correta. list(list, int) -> list'''
    lista_crescente = (lista_numero[0]) + ([lista_numero[1]])
    lista_sort = list.sort(lista_crescente)
    return lista_sort
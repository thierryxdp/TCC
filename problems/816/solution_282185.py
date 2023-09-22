def maiores(lista, n):
    '''Função que retorna uma lista ordenada com os números maiores que n fornecidos'''
    '''list, int -> list'''
    list.insert(lista,0,n)
    list.sort(lista)
    local_De_n = list.index(lista,n)
    nobalist = lista[local_De_n+1:]
    return nobalist
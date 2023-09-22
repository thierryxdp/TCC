def maiores(lista,n):
    ''' Essa função recebe uma lista e um numero inteiro e retorna apenas os numeros da lista maiores que n.'''
    ''' Entrada = lista ; saída = lista'''
    n = [n]
    lista_nova = lista + n
    lista2 = list.sort(lista_nova)
    [n] = n 
    return lista_nova[[n]+1:]
def maiores(lista,n):
    ''' Essa função recebe uma lista e um numero inteiro e retorna apenas os numeros da lista maiores que n.'''
    ''' Entrada = lista ; saída = lista'''
    n = [n]
    lista_nova = lista + n
    lista2 = list.sort(lista_nova)
    er = lista[n]
    lista3 = lista_nova[er:]
    return lista3
def maiores(lista,n):
    ''' Essa função recebe uma lista e um numero inteiro e retorna apenas os numeros da lista maiores que n.'''
    ''' Entrada = lista ; saída = lista'''
    n = [n]
    nova_lista = lista + n
    lista2 = list.sort(nova_lista)
    lista3 = lista2[n+1:]
    return lista3
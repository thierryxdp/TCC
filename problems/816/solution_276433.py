def maiores(lista_numeros,n):
    '''Função que, dada uma lista de números e um número n, retorna uma outra lista com somente os membros da primeira lista maiores que n.
    list, int --> list'''
    list.append(lista_numeros,n)
    list.sort(lista_numeros)
    return lista_numeros[(list.index(lista_numeros,n)+1):]
def maiores(lista_numeros,n):
    '''Funcao que, dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista com numeros maiores que n.list,int->list.'''
    lista_numeros.append(n+1)
    lista_numeros.sort()
    p = lista_numeros.index(n+1)
    return lista_numeros[p+1:]
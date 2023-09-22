def maiores(lista_numeros,n):
    '''list,int->list.'''
    lista_numeros.append(n+1)
    lista_numeros.sort()
    posicao = lista_numeros.index(n+1)
    return lista_numeros[posicao+1:]
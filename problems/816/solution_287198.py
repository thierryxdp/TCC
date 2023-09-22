def maiores(lista,n):
    '''Função que dada uma lista e um numero n retorne uma lista com os numeros maiores que n;list,int->list'''
    lista1=list.append(lista,n)
    list.sort(lista1)
    i=list.index(lista1,n)
    return lista1[i:]
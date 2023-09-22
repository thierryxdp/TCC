def maiores(lista,n):
    '''Função que dada uma lista e um numero n retorne uma lista com os numeros maiores que n;list,int->list'''
    lista1=list.append(lista,n)
    lista2=list.sort(lista1)
    i=list.index(lista2,n)
    return lista2[i:]
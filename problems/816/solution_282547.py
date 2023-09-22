def insere(lista_numero,n):
    '''dada uma lista com numeros ordenados e um numero n, posiciona o numero n na posicao correta para a lista continuar ordenada;
    list->list'''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista,n):
    '''dada uma lista com numeros ordenados e um numero n, posiciona o numero n na posicao correta para a lista continuar ordenada removendo os numeros menores que n;
    list->list'''
    insere(lista,n)
    a=list.index(lista,n)
    del lista[:a+1]
    return lista
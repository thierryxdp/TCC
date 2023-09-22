def insere(lista_numero,n):
    '''data uma lista com numeros ordenados e um numero n, posiciona o numero n na posicao correta para a lista continuar ordenada;
    list->list'''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista,n):
    insere(lista,n)
    a=list.count(lista,n)
    return del lista[:a]
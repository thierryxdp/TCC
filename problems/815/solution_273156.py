def insere(lista_numero,n):
    '''dada uma lista ordenada (crescente) de ńumeros inteiros e um ńumero inteiro n,
incli N na posic̃ao correta. list,int->list'''
    lista_numero.append(n)
    ordenada = list.sort(lista_numero)
    return lista_numero
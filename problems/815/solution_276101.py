def insere(lista_numero,n):
    'dada uma lista ordenada crescente de num inteiros e um numero n qq,inclui esse Numero na lista,mantendo a ordenacao'
    'lista,int---lista'
    lista_numero+=[n, ]
    lista_numero.sort()
    return lista_numero
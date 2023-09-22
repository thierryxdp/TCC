def insere(lista,n):
    '''funcao que dada uma lista insere um numero inteiro (n) de modo que a lista continue ordenada'''
    lista = lista.append(n)
    lista= ''.sort(lista)
    return lista
def insere(lista_numero,n):
    '''
    dada uma lista ordenada crescente e um numero, inclua n na posicao certa, mantendo a lista ordenada
    str, int -> str
    '''
    lista_numero.append(n)
    return lista_numero.sort()
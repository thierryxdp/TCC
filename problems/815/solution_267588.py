def insere(lista_numero,n):
    '''funç˜ao insere(lista numero, n) que dada uma lista ordenada (crescente)
    de números inteiros e um número inteiro n, inclua n na posiç˜ao correta, ou seja,
    de tal maneira que a lista continue ordenada.
    lista,int->lista '''
    x=list.append(lista_numero,n)
    y=list.sort(lista_numero)
    return lista_numero
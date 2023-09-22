def insere(lista_numero, n):
    '''função que, dada uma lista ordenada (crescente) de números inteiros e um inteiro n,
    retorne o n na posiçao correta, para manter a lista ordenada; list,int ->  '''
    a=lista_numero
    list.extend(lista_numero, [n])
    a.sort()
    return a
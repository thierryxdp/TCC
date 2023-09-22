def insere(lista_numero,n):
    '''Dada uma lista ordenada (crescente) de números inteiros e um número inteiro n, inclua n na posição correta, mantendo a lista ordenada.
assinatura: list --> list'''
    list.insert(lista_numero,0,n)
    list.sort(lista_numero)
    return lista_numero
def insere(lista_numero, n):
    '''Dada uma lista ordenada (crescente) de números inteiros e 
    um número inteiro n, a função inclui esse número na posição correta, ou seja, 
    de forma ordenada.'''
    lista = lista_numero
    lista.append(n)
    lista.sort()
    return lista
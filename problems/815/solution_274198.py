def insere(lista_numero, n):
    '''Função que dada uma lista ordenada (crescente) de números inteiros e um número inteiro n, inclua n na posição correta.
    list -> list'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero
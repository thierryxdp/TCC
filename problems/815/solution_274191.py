def insere(lista_numero, n):
    '''Função que dada uma lista ordenada (crescente) de números inteiros e um número inteiro n, inclua n na posição correta.
    list -> list'''
    lista = list.append(lista_numero, n)
    lista = list.sort(lista)
    return lista
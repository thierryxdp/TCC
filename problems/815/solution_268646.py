def insere(lista_numero,n):
    '''Função que dada uma lista ordenada(crescente) de números inteiros e um número inteiro n
    inclua n na posição correta'''
    lista=[lista_numero+n]
    return list.sort(lista)
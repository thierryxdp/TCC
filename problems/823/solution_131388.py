def faltante(lista):
    '''Função que dada uma lista de números inteiros de entrada, retorna o
    inteiro que está faltando para completar essa lista.'''
    pecas = len(lista) + 1
    list.sort(lista)
    contador = 0
    while contador < pecas:
        if contador + 1 not in lista:
            return contador + 1
        if lista[contador] != contador + 1:
            return contador + 1
        else:
            contador = contador + 1
    return contador
def faltante(lista_faltando):
    '''dada uma lista com N − 1 inteiros numerados de 1 a N, 
    descobre qual número inteiro deste intervalo está faltando.
    Entrada: lista L de tamanho N-1 contendo números inteiros (não repetidos) de 1 a N.
    Saída: função deve retornar o número inteiro x que pertence ao intervalo [1, N] mas que nao pertence a lista de entrada L.'''
    list.sort(lista_faltando)
    indice = 0
    while indice < len(lista_faltando) and lista_faltando[indice] == indice + 1:
        indice = indice + 1
    return indice + 1
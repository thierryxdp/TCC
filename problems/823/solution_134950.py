def faltante (pecas):
    '''funcao que retorna o numero  inteiro x que pertence ao intervalo [1,N] mas que pertence a lista de entrada int -> int'''
    list.sort(pecas)
    contador= n+1
    while contador <len(pecas):
        if pecas[contador]==contador+1:
            return contador
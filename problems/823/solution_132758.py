def faltante(pecas):
    '''função que retorna a peça faltante de uma lista com os
    numeros das peças do jogo
    list -> int'''
    list.sort(pecas)
    i = 1
    while i < len(pecas):
        if pecas[i] != pecas[i-1] + 1:
            return pecas[i] - 1
        i += 1
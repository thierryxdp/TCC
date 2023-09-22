def faltante(pecas):
    '''função que retorna a peça faltante de uma lista com os
    numeros das peças do jogo
    list -> int'''
    list.sort(pecas)
    if pecas[0] == 2:
        return 1
    elif len(pecas) == 1:
        return 2
    elif pecas[-1] == len(pecas):
        return pecas[-1] + 1
    else:
 	    i = 1
    	while i < len(pecas):
            if pecas[i] != pecas[i-1] + 1:
                return pecas[i] - 1
            i += 1
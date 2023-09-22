def pontos_por_time(jogo):
    ''' retorna o numero total de pontos de cada time
    dadas duas listas dos jogos de ida  e volta
    list, list -> dict'''
    nome1=jogo[0]
    nome2=jogo[1]
    if jogo[0][2] > jogo[0][3] and jogo[0][2] < jogo[0][3]:
        pt1 = 6
        pt2 = 0
        return {nome1:pt1, nome2:pt2}
    elif jogo[2][0] < jogo[2][1] and jogo[2][0] > jogo[2][1]:
        pt1 = 0
        pt2 = 6
        return {nome1:pt1, nome2:pt2}
    elif jogo[2][0] > jogo[2][1] and jogo[2][0] == jogo[2][1]:
        pt1 = 4
        pt2 = 1
        return {nome1:pt1, nome2:pt2}
    elif jogo[2][0] < jogo[2][1] and jogo[2][0] == jogo[2][1]:
        pt1 = 1
        pt2 = 4
        return {nome1:pt1, nome2:pt2}
    elif jogo[2][0] == jogo[2][1] and jogo[2][0] < jogo[2][1]:
        pt1 = 4
        pt2 = 1
        return {nome1:pt1, nome2:pt2}
    elif jogo[2][0] == jogo[2][1] and jogo[2][0] > jogo[2][1]:  
        pt1 = 1
        pt2 = 4        
        return {nome1:pt1, nome2:pt2}
    elif jogo[2][0] > jogo[2][1] and jogo[2][0] > jogo[2][1]:
        pt1 = 3
        pt2 = 3
        return {nome1:pt1, nome2:pt2}
    elif jogo[2][0] < jogo[2][1] and jogo[2][0] < jogo[2][1]:
        pt1 = 3
        pt2 = 3
        return {nome1:pt1, nome2:pt2}
    else:
        pt1 = 2
        pt2 = 2
        return {nome1:pt1, nome2:pt2}
def pontos_por_time(jogoi, jogov):
    ''' retorna o numero total de pontos de cada time
    dadas duas listas dos jogos de ida  e volta
    list, list -> dict'''
    nome1=jogoi[0]
    nome1=jogoi[1]
    if jogoi[2][0] > jogoi[2][1] and jogov[2][0] < jogov[2][1]:
        pt1 = 6
        pt2 = 0
        return {nome1:pt1, nome2:pt2}
    elif jogoi[2][0] < jogoi[2][1] and jogov[2][0] > jogov[2][1]:
        pt1 = 0
        pt2 = 6
        return {nome1:pt1, nome2:pt2}
    elif jogoi[2][0] > jogoi[2][1] and jogov[2][0] == jogov[2][1]:
        pt1 = 4
        pt2 = 1
        return {nome1:pt1, nome2:pt2}
    elif jogoi[2][0] < jogoi[2][1] and jogov[2][0] == jogov[2][1]:
        pt1 = 1
        pt2 = 4
        return {nome1:pt1, nome2:pt2}
    elif jogoi[2][0] == jogoi[2][1] and jogov[2][0] < jogov[2][1]:
        pt1 = 4
        pt2 = 1
        return {nome1:pt1, nome2:pt2}
    elif jogoi[2][0] == jogoi[2][1] and jogov[2][0] > jogov[2][1]:  
        pt1 = 1
        pt2 = 4        
        return {nome1:pt1, nome2:pt2}
    elif jogoi[2][0] > jogoi[2][1] and jogov[2][0] > jogov[2][1]:
        pt1 = 3
        pt2 = 3
        return {nome1:pt1, nome2:pt2}
    elif jogoi[2][0] < jogoi[2][1] and jogov[2][0] < jogov[2][1]:
        pt1 = 3
        pt2 = 3
        return {nome1:pt1, nome2:pt2}
    else:
        pt1 = 2
        pt2 = 2
        return {nome1:pt1, nome2:pt2}
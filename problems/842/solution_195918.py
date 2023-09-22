def pontos_por_time(jogoi, jogov):
    ''' retorna o numero total de faltas de cada time
    dadas duas listas dos jogos de ida  e volta
    list, list -> dict'''

    nome_t1=jogoi[0]
    nome_t2=jogov[0]
    if jogoi[2][0] > jogoi[2][1]:
        pt1 = 3
        pt2 = 0
    elif jogoi[2][0] < jogoi[2][1]:
        pt1 = 0
        pt2 = 3
    else:
        pt1 = 1
        pt2 = 1
    if jogov[2][0] > jogov[2][1]:
    pt1 = pt1+3
    pt2 = pt2+0
    elif jogov[2][0] < jogov[2][1]:
    pt1 = pt1+0
    pt2 = pt2+3
    else:
    pt1 = pt1+1
    pt2 = pt2+1
    return {nome_t1:pt1, nome_t2:pt2}
def pontos_por_time1(jogoi, jogov):
    ''' retorna o numero total de pontos de cada time
    dadas duas listas dos jogos de ida  e volta
    list, list -> dict'''

    nome_t1 = jogoi[0]
    nome_t2 = jogov[0]
    pontos_t1 = jogoi[2][0] + jogov[2][1]
    pontos_t2 = jogoi[2][1] + jogov[2][0]
    
    return {nome_t1:pontos_t1, nome_t2:pontos_t2}


def pontos_por_time2(jogoi, jogov):
    ''' retorna o numero total de pontos de cada time
    dadas duas listas dos jogos de ida  e volta
    list, list -> dict'''

    pontos_t1 = jogoi[2][0] + jogov[2][1]
    pontos_t2 = jogoi[2][1] + jogov[2][0]
    
    return {jogoi[0]:pontos_t1, jogov[0]:pontos_t2}
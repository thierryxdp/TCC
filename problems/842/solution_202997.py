def faltas_por_time2(jogoi, jogov):
    ''' retorna o numero total de faltas de cada time
    dadas duas listas dos jogos de ida  e volta
    list, list -> dict'''

    faltas_t1 = jogoi[2][0] + jogov[2][1]
    faltas_t2 = jogoi[2][1] + jogov[2][0]
    
    return {jogoi[0]:faltas_t1, jogov[0]:faltas_t2}#Start your python function here
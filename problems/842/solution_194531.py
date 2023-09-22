def pontos_por_time(jogoi, jogov):
    ''''''

    faltas_t1 = jogoi[2][0] + jogov[2][1]
    faltas_t2 = jogoi[2][1] + jogov[2][0]
    
    return {jogoi[0]:faltas_t1, jogov[0]:faltas_t2}
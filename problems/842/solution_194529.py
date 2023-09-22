def pontos_por_time(jogoi, jogov):
    '''list, list -> dict'''

    nome_t1=jogoi[0]
    nome_t2=jogov[0]
    faltas_t1 = jogoi[2][0] + jogov[2][1]
    faltas_t2 = jogoi[2][1] + jogov[2][0]
    
    return {nome_t1:faltas_t1, nome_t2:faltas_t2}
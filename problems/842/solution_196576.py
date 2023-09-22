def pontos_por_time(jogos):
    nome_t1=jogos[0][0]
    nome_t2=jogos [1][0]
    pontos1= jogos[0][2][0] + jogos[1][2][1]
    pontos2= jogos[0][2][1] + jogos[1][2][0]

    return {nome_t1:pontos1, nome_t2:pontos2}
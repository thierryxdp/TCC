def pontos_por_time(jogos):
    nome_t1=jogos[0][0]
    nome_t2=jogos [1][0]
    pontos1= jogos[0][2][0] + jogos[1][2][1]
    pontos2= jogos[0][2][1] + jogos[1][2][0]
    if pontos1>pontos2:
        return {nome_t1:6, nome_t2:0}
    if pontos2>pontos1:
        return {nome_t2:6, nome_t1:0}
    if pontos1==pontos2:
        return {nome_t1:1, nome_t2:1}
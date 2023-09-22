def pontos_por_time(jogos):
    """Dadas as entradas em formato de lista, representando as partidas de ida e volta entre 'cormengo', e 'flamínthians', retornar a pontuação de cada time"""
    time_1=jogos[0][0]
    time_2=jogos[0][1]
    pontuacao_t1=[]
    pontuacao_t2=[]
    resultado_t1=sum(pontuacao_t1)
    resultado_t2=sum(pontuacao_t2)
    if jogos[0][2][0]==jogos[0][2][1]:
        pontuacao_t1=pontuacao_t1+[1]
        pontuacao_t2=pontuacao_t2+[1]
    if jogos[0][2][0]>jogos[0][2][1]:
        pontuacao_t1=pontuacao_t1+[3]
    if jogos[0][2][0]<jogos[0][2][1]:
        pontuacao_t2=pontuacao_t2+[3]
    if jogos[1][2][0]==jogos[1][2][1]:
        pontuacao_t1=pontuacao_t1+[1]
        pontuacao_t2=pontuacao_t2+[1]
    if jogos[1][2][0]>jogos[1][2][1]:
        pontuacao_t2=pontuacao_t2+[3]
    if jogos[1][2][0]<jogos[1][2][1]:
        pontuacao_t1=pontuacao_t1+[3]
    return {time_1:resultado_t1,time_2:resultado_t2}
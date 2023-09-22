def pontos_por_time(jogo_i,jogo_v):
    """Dadas as entradas em formato de lista, representando as partidas de ida e volta entre 'cormengo', e 'flamínthians', retornar a pontuação de cada time"""
    time_1=jogo_i[0]
    time_2=jogo_v[0]
    pontuacao_t1=[]
    pontuacao_t2=[]
    resultado_t1=sum(pontuacao_t1)
    resultado_t2=sum(pontuacao_t2)
    if jogo_i[2][0]==jogo_i[2][1]:
        pontuacao_t1=pontuacao_t1+[1]
        pontuacao_t2=pontuacao_t2+[1]
    if jogo_i[2][0]>jogo_i[2][1]:
        pontuacao_t1=pontuacao_t1+[3]
    if jogo_i[2][0]<jogo_i[2][1]:
        pontuacao_t2=pontuacao_t2+[3]
    if jogo_v[2][0]==jogo_v[2][1]:
        pontuacao_t1=pontuacao_t1+[1]
        pontuacao_t2=pontuacao_t2+[1]
    if jogo_v[2][0]>jogo_v[2][1]:
        pontuacao_t2=pontuacao_t2+[3]
    if jogo_v[2][0]<jogo_v[2][1]:
        pontuacao_t1=pontuacao_t1+[3]
    return {time_1:resultado_t1,time_2:resultado_t2}
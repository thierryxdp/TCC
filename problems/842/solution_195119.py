def pontos_por_time(jogos):
    jogo1=jogos[0]
    jogo2=jogos[1]
    gols1=jogo1[2]
    gols2=jogo2[2]
    time1=jogo1[0]
    time2=jogo1[1]
    pts_t1=0
    pts_t2=0
    if gols1[0]>gols1[1]:
        pts_t1=pts_t1+3
    elif gols1[0]<gols1[1]:
        pts_t2=pts_t2+3
    else:
        pts_t1=pts_t1+1
        pts_t2=pts_t2+1
    if gols2[0]>gols2[1]:
        pts_t2=pts_t2+3
    elif gols2[0]<gols2[1]:
        pts_t1=pts_t1+3
    else:
        pts_t1=pts_t1+1
        pts_t2=pts_t2+1
    resultados={time1:pts_t1,time2:pts_t2}
    return resultados
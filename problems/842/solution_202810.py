#Start your python function here
def pontos_por_time(time1,time2,placar1,placar2):
    t1=time1
    t2=time2
    p1=placar1
    p2=placar2
    jogo={t1:time1,
          p1:placar1}
    jogo2={t2:time2,
           p2:placar2}
    return jogo[t1]+jogo[p1]+jogo2[t2]+jogo2[p2]
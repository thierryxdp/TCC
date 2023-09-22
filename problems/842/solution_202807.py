#Start your python function here
def pontos_por_time(time1,time2,placar1,placar2):
    jogo={time1:time1,
          time2:time2,
          placar1:placar1,
          placar2:placar2}
    return jogo[time1]+jogo[time2]
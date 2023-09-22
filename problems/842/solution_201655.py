def pontos_por_time(time1,time2):
    '''retorna os pontos que cada time1 ganhou em 2 partidas contra o outro time2 e vice versa baseado no numero de gols list,list-.dic'''
    if [time1,time2[0]] = [time1,time2[1]] and [time2,time1[0]] = [time2,time1[1]]:
        return { time1: 2, time2: 2 }
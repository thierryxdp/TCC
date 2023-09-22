def pontos_por_time(fase):
    p = {fase[0][0]: 0, fase[0][1]: 0}
    ida = pontuacao(fase[0])
    contador(p,ida)
    volta = pontuacao(fase[1])
    contador(p,volta)
    return p

def pontos(fase):
    time1 = fase[0]
    time2 = fase[1]
    gtime1 = fase[2][0]
    gtime2 = fase[2][1]
    if gtime1 < gtime2:
        return (time1, 0, time2, 3)
    if gtime1 > gtime2:
        return (time1, 3, time2, 0)
    return (time1, 1, time2, 1)

p = {'cor':3,'fla':0}

def contador(p,t):
    time1 = t[0]
    time2 = t[2]
    p[time1] = p[time1] + t[1]
    p[time2] = p[time2] + t[3]
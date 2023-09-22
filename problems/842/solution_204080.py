#Start your python function here
def pontos_por_time(jogos):
    time1 = jogos[0] [0]
    time2 = jogos[0] [1]
    gj1t1 = jogos[0] [2] [0]
    gj1t2 = jogos[0] [2] [1]
    gj2t1 = jogos[1] [2] [0]
    gj2t2 = jogos[1] [2] [1]
    ptstime1 = 0
    ptstime2 = 0
    if gj1t1 > gj1t2:
        ptstime1 += 3
    if gj1t1 < gj1t2:
        ptstime2 += 3 
    if gj1t1 == gj1t2:
        ptstime1 += 1 and ptstime2 += 1
    if gj2t1 > gj2t2:
        ptstime1 += 3
    if gj2t1 < gj2t2:
        ptstime2 += 3 
    if gj2t1 == gj2t2:
        ptstime1 += 1 and ptstime2 += 1
    totalpts = {time1:ptstime1,time2:ptstime2}
    return totalpts
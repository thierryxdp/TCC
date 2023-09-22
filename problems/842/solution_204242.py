def pontos_por_time(a):
    return time1 + time2
def jogo1(a):
    return a[0]
def jogo2(a):
    return a[1]
def gols1(a):
    return jogo1(a)[2]
def gols2(a):
    return jogo2(a)[2]
def res1(a):
    if gols1(a)[0] > gols1(a)[1]:
        tim1=3
        tim2=0
    if gols1(a)[0]<gols1(a)[1]:
        tim1=0
        tim2=3
    else:
        tim1=1
        tim2=1

    def res2(a):
        if gols2(a)[0] > gols2(a)[1]:
        time1=tim1+3
        if gols2(a)[0]<gols2(a)[1]:
        time2=tim2+3
        else:
        time1=tim1+1
        time2=tim2+1
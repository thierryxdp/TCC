def pontos_por_time(a):
    return res1(a) + res2(a)
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
        time1=3
        time2=0
    if gols1(a)[0] =gols1(a)[1]:
        time1=1
        time2=1
    else:
        time1=0
        time2=3
def res2(a):
    if gols2(a)[0] > gols2(a)[1]:
        time1=time1+3
        time2=time2
    if gols2(a)[0] =gols2(a)[1]:
        time1=time1+1
        time2=time2+1
    else:
        time1=time1
        time2=time2+3
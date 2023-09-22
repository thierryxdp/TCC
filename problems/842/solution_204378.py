def pontos_por_time(v,e):
    return 3*v+e
def jogo(L):
    time1=L[0[0]]
    time2=L[0[1]]
    p1=int
    p2=int
    if time1==L[1[0]]:
        p1= pontos_por_time(L[0[2[0]]],L[1[2[0]]])
        p2= pontos_por_time(L[0[2[1]]],L[1[2[1]]])
    if time2==L[1[0]]:
        p1= pontos_por_time(L[0[2[1]]],L[1[2[1]]])
        p2= pontos_por_time(L[0[2[0]]],L[1[2[0]]])
        return dict(time1=p1, time2=p2)#Start your python function here
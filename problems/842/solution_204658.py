def jogo(a,b):
    if a>b:
        return 3
    if a==b:
        return 1 
def pontos_por_time(l):
    d={}
    pontosTime1= jogo(l[0][2][0],l[0][2][1])+jogo(l[1][2][1],l[1][2][0])
    pontosTime2= (jogo(l[0][2][1],l[0][2][0]))+(jogo(l[1][2][0],l[1][2][1]))
    Time1= l[0][0]
    Time2= l[0][1]
    d=dict(Time1=pontosTime1,Time2=pontosTime2)
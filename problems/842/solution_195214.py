def pontos_por_time(lista):
    '''Funcao que, dados dois times e suas quantidades de gols, retorna um dicionário com o nome do time e sua pontuação; lista com duas listas dentro dessa, dentro das quais tem os nomes dos times e suas quantidades de gols'''
    [[time1, time2, [gols1p1, gols2p1]], [time1, time2, [gols1p2, gols2p2]]]=lista
    pontuacao={}
    a=gols1p1>gols2p1
    b=gols1p1==gols2p1
    c=gols1p1<gols2p1
    d=gols1p2>gols2p2
    e=gols1p2==gols2p2
    f=gols1p2<gols2p2
    if a and d:
        pontuacao={time1:3*2, time2:0}
    elif (a and f) or (c and d):
        pontuacao={time1:3, time2:3}
    elif c and f:
        pontuacao={time1:0, time2:3*2}
    elif (b and d) or (a and e):
        pontuacao={time1:4, time2:1}
    elif (b and f) or (c and e):
        pontuacao={time1:1, time2:4}
    elif b and e:
        pontuacao={time1:2, time2:2}
    return pontuacao
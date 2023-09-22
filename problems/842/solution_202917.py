def pontos_por_time(L1):
    """recebe uma lista no formato L1 abaixo e retorna os nomes dos times com seus respectivos totais de pontos.
OBS: L1= [["time1", "time2",[gol1,gol2]],["time2","time1",[gol2,gol1]]].
list->dict"""
    pts1=0
    pts2=0
    pts1b=0
    pts2b=0
    if L1[0][2][0]> L1[0][2][1]:
        pts1=3
    elif L1[0][2][0]< L1[0][2][1]:
        pts2=3
    elif int(L1[0][2][0])- int(L1[0][2][1])==0:
        pts1=1
        pts2=1
    if L1[1][2][1]> L1[1][2][0]:
        pts1b=3
    elif L1[1][2][0]> L1[1][2][1]:
        pts2b=3
    elif int(L1[1][2][0])- int(L1[1][2][1])==0:
        pts1b=1
        pts2b=1
    dici= {L1[0][0]:int(pts1)+int(pts1b),L1[0][1]:int(pts2)+int(pts2b)}
    return dici
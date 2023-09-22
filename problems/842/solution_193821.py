def pontos_por_time (x):
###testar###
    [ [time1,time2,[ponto1,ponto2]] ,[time2,time1,[ponto3,ponto4]] ] = x

# time 1 = ponto 1 e ponto 4
# time 2 = ponto 2 e ponto 3

    if ponto1 > ponto2 and ponto4 > ponto3:
        p1= + 6
        p2 = 0
    elif ponto2 > ponto1 and ponto3 > ponto4:
        p2 = +6
        p1 = 0
    elif ponto1 == ponto2 and ponto3 == ponto4:
        p1 = +2
        p2 = +2
    elif ponto1 > ponto2 and ponto4 < ponto3:
        p1 = +3
        p2 = +3
    elif ponto1 < ponto2 and ponto4 > ponto3:
        p1 = +3
        p2 = +3
    elif ponto1 == ponto2 and ponto4 < ponto3:
        p1 = +1
        p2 = +4
    elif ponto1 == ponto2 and ponto4 > ponto3:
        p1 = +4
        p2 = +1
    elif ponto1 > ponto2 and ponto4 == ponto3:
        p1 = +4
        p2 = +1
    elif ponto1 < ponto2 and ponto4 == ponto3:
        p1 = +1
        p2 = +4

    return {time1:p1,time2:p2}
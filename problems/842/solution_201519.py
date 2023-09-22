def pontos_por_time(lis):
    pnt11 = lis[0][2][0]
    pnt12 = lis[0][2][1]
    pnt21 = lis[1][2][0]
    pnt22 = lis[1][2][1]
    time1 = 0
    time2 = 0
    if pnt11 > pnt12:
        time1 = time1 + 3
    else:
        time2 = time2 + 3
    if pnt21 < pnt22:
        time1 = time1 + 3
    else:
        time2 = time2 + 3
    return time1
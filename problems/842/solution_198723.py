def pontos_por_time(l1):
    dicio1={str(l1[1][0]): 0, str(l1[0][0]): 6}
    dicio2={str(l1[0][0]): 6, str(l1[1][0]): 0}
    if l1[0][2][1] or l1[1][2][0] > l1[0][2][0] or l1[1][2][1]:
        return dicio2
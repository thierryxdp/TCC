def pontos_por_time(ls):
    gls_time1_1=ls[0][2][0]
    gls_time1_2=ls[1][2][1]
    gls_time2_1=ls[0][2][1]
    gls_time2_2=ls[1][2][0]
    if gls_time1_1>gls_time2_1 and gls_time1_2>gls_time2_2:
        return 'Time 1: 6 pontos'
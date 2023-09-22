def pontos_por_time(k):
    k = [['time1','time2',[a1,b1]],['Time2','Time1',[b2,a2]]]
    r1 = [a1,b1]
    r2 = [b2,a2]
    if (r1[0]==r2[1]):
        return ['time1':6,'time2':0]
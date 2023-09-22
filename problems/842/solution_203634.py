def pontos_por_time(lista):
    j1= lista[0]
    j2= lista[1]
    time1= j1[0]
    time2= j2[0]
    gols1= j1[2]
    gols2= j2[2]
    v1= gols1[0]-gols1[1]
    v2= gols2[1]-gols2[0]
    if v1<0 and v2<0:
        return {time1:0,time2:6}
    elif v1>0 and v2>0:
        return {time1:6,time2:0}
    elif v1==0 and v2==0:
        return {time1:2,time2:2}
    elif v1<0 and v2==0:
        return {time1:1,time2:4}
    elif v1==0 and v2<0:
        return {time1:1,time2:4}
    elif v1>0 and v2==0:
        return {time1:4,time2:1}
    elif v1==0 and v2>0:
        return {time1:4,time2:1}
    else:
        return {time1:3,time2:3}

#Start your python function here
def pontos_por_time(lista1):
    a=lista1[0][2][0]
    b=lista1[0][2][1]
    c=lista1[1][2][0]
    d=lista1[1][2][1]
    time1= lista1[0][0]
    time2= lista1[0][1]
    lista1= [[time1, time2, [a, b]], [time1, time2,[c, d]]]
    
    if (a==b) and (c==d):
        return {time1: 2,
                time2: 2}
    elif (a>b) and (c>d):
        return {time1: 6,
                time2: 0}
    elif (a<b) and (c<d):
        return {time1: 0,
                time2: 6}
    elif (a>b) and (c==d):
        return {time1: 4,
                time2: 1}
    elif (a<b) and (c==d):
        return {time1: 1,
                time2: 4}
    elif (a==b) and (c>d):
        return {time1: 4,
                time2: 1}
    elif (a==b) and (c<d):
        return {time1: 1,
                time2: 4}
    elif (a>b) and (c<d):
        return {time1: 3,
                time2: 3}
    elif (a<b) and (c>d):
        return {time1: 3,
                time2: 3}
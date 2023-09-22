def pontos_por_time (ls):
    time1=ls[0][0]
    time2=ls[0][1]
    t1j1=ls[0][2][0]
    t2j1=ls[0][2][1]
    t1j2=ls[1][2][1]
    t2j2=ls[1][2][0]
    if t1j1>t2j1:
        if t1j2>t2j2:
            return {time1:6,time2:0}
        if t1j2==t2j2:
            return {time1:4,time2:1}
        if t1j2<t2j2:
            return {time1:3,time2:3}
    if t1j1==t2j1:
        if t1j2>t2j2:
            return {time1:4,time2:1}
        if t1j2==t2j2:
            return {time1:2,time2:2}
        if t1j2<t2j2:
            return {time1:1,time2:4}
    if t1j1<t2j1:
        if t1j2>t2j2:
            return {time1:3,time2:3}
        if t1j2==t2j2:
            return {time1:1,time2:4}
        if t1j2<t2j2:
            return {time1:0,time2:6}
def pontos_por_time(lista):
    [time1,time2,[gol11,gol21]]=lista[0]
    [time2,time1,[gol22,gol12]]=lista[1]
    if gol11==gol21:
        if gol22==gol12:
            return {time2:2,time1:2}
        elif gol22>gol12:
            return {time2:1,time1:4}
        elif gol12>gol22:
            return {time1:4,time2:1}
    if gol11>gol21:
        if gol22==gol12:
            return {time2:1,time1:4}
        elif gol22>gol12:
            return {time2:3,time1:3}
        elif gol12>gol22:
            return {time2:0,time1:6}
    if gol21>gol11:
        if gol22==gol12:
            return {time2:4,time1:1}
        elif gol22>gol12:
            return {time2:6,time1:0}
        elif gol12>gol22:
            return {time2:3,time1:3}
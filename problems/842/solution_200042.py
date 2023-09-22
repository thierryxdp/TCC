def pontos_por_time(pt_jogo):

    ida = pt_jogo[0]
    volta = pt_jogo[1]

    time1 = ida[0]
    time2 = ida[1]

    gF_ida = ida[2][1] 
    gC_ida = ida[2][0]
    gF_volta = volta[2][0]
    gC_volta = volta[2][1]
    if (gC_ida > gF_ida) and (gC_volta > gF_volta):
        return {time1: 6, time2: 0}
    elif (gF_ida == gC_ida) and (gF_volta == gC_volta):
        return {time1: 2, time2: 2}
    elif (gC_ida > gF_ida) and (gC_volta < gF_volta):
        return {time1: 3, time2: 3}
    elif (gC_ida < gF_ida) and (gC_volta < gF_volta):
        return {time1: 0, time2: 6}
    elif (gC_ida < gF_ida) and (gC_volta > gF_volta):
        return {time1: 3, time2: 3}
    elif (gC_ida < gF_ida) and (gC_volta == gF_volta):
        return {time1: 1, time2: 4}
    elif (gC_ida > gF_ida) and (gC_volta == gF_volta):
        return {time1: 4, time2: 1}
    elif (gC_ida == gF_ida) and (gC_volta < gF_volta):
        return {time1: 1, time2: 4}
    else:
        return {time1: 4, time2: 1}
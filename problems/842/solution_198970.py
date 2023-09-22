#Start your python function heredef pontos(pto_jogo):

    ida = pto_jogo[0]
    volta = pto_jogo[1]

    time1 = ida[0]
    time2 = ida[1]

    gF_ida = ida[2][1] 
    gC_ida = ida[2][0]
    gF_volta = volta[2][0]
    gC_volta = volta[2][1]
    
    if gF_ida < gC_ida:
        cv = 3
        fv = 0
    elif gF_ida > gC_ida:
        cv = 0
        fv = 3    
    elif gF_volta < gC_volta:
        cv = 3
        fv = 0
    else:
        cv = 0
        fv = 3

    if gF_ida == gC_ida:
        ce = 1
        fe = 1
    elif gF_volta == gC_volta:
        ce = 1
        fe = 1
    else:
        ce = 0
        fe = 0

    t_ptos_f = fv + fe
    t_ptos_c = cv + ce
    
    return {time1: t_ptos_c, time2: t_ptos_f}
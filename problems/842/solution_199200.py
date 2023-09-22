#Start your python function here

def pontos_por_time(pto_jogo):

    ida = pto_jogo[0]
    volta = pto_jogo[1]

    time1 = ida[0]
    time2 = ida[1]

    gF_ida = ida[2][1] 
    gC_ida = ida[2][0]
    gF_volta = volta[2][0]
    gC_volta = volta[2][1]
    
    if (gF_ida == gC_ida) or (gF_volta == gC_volta):
        c_ida = 1
        f_ida = 1
        c_volta = 1
        f_volta = 1

    else:
        c_ida = 0
        f_ida = 0
        c_volta = 0
        f_volta = 0
        
    if (gF_ida < gC_ida) or (gF_volta < gC_volta):
        c_ida = 3
        f_ida = 0
        c_volta = cv_ida
        f_volta = fv_ida
    else:
        c_ida = 0
        f_ida = 3
        c_volta = cv_ida
        f_volta = fv_ida
           
    pF_ida = f_ida + f_ida
    pF_volta = f_volta + f_volta

    pC_ida = c_ida + c_ida
    pC_volta = c_volta + c_volta

    t_ptos_f = pF_ida + pF_volta
    t_ptos_c = pC_ida + pC_volta
    
    return {time2: t_ptos_f, time1: t_ptos_c}
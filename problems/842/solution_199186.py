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
        ce_ida = 1
        fe_ida = 0
        ce_volta = 1
        fe_volta = 0

    else:
        ce_ida = 0
        fe_ida = 0
        ce_volta = 0
        fe_volta = 0
        
    if (gF_ida < gC_ida) or (gF_volta < gC_volta):
        cv_ida = 3
        fv_ida = 0
        cv_volta = cv_ida
        fv_volta = fv_ida
    else:
        cv_ida = 0
        fv_ida = 3
        cv_volta = cv_ida
        fv_volta = fv_ida
           
    pF_ida = fv_ida + fe_ida
    pF_volta = fv_volta + fe_volta

    pC_ida = cv_ida + ce_ida
    pC_volta = cv_volta + ce_volta

    t_ptos_f = pF_ida + pF_volta
    t_ptos_c = pC_ida + pC_volta
    
    return {time2: t_ptos_f, time1: t_ptos_c}
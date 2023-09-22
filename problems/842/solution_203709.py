def pontos(x):
    gols_1 = x[0]
    gols_2 = x[1]
    if gols_1 > gols_2:
        [3,0]
    if gols_1 == gols_2:
        [1,1]
    if gols_1 < gols_2:
        [0,3]

def pontos_por_time(x):
    jg1 = x[0]
    jg2= x[1]
    
    t1 = x[0][0]
    t2 = x[0][1]
    
    gols_1_1 = jg1[2][0]
    gols_2_1 = jg1[2][1]
    gols_1_2 = jg2[2][0]
    gols_2_2 = jg2[2][1]
    
    if gols_1_1 and gols_1_2 > gols_1_2 and gols_2_2:
        pt= (6,0)
    elif gols_1_1 > gols_1_2 and gols_1_2 == gols_2_2:
        pt=(4,1)
    elif gols_1_1 == gols_1_2 and gols_1_2 == gols_2_2:
        pt =(1,1)
    
    
    pt_t1 = pt[0] + pt[1]
    pt_t2 = pt[1] + pt[0]
    
    return {t2:pt_tim2,t1:pt_t1}
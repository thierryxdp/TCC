def pontos_por_time(x):
    gols_1 = x[0]
    gols_2 = x[1]
    if gols_1 > gols_2:
		[3,0]
    if gols_1 == gols_2:
        [1,1]
    if gols_1 < gols_2:
        [0,3]

def pt_times(x):
    jg1 = x[0]
    jg2= x[1]
    
    t1 = x[0]
    t2 = x[1]
    
    gols_1_1 = jg1[2][0]
    gols_2_1 = jg1[2][1]
    gols_1_2 = jg2[2][0]
    gols_2_2 = jg2[2][1]
    
    pt_jogo1 = pontos([gols_1_1, gols_2_1])
    pt_jogo2 = pontos([gols_1_2, gols_2_2])
    
    pt_t1 = pontos[0] + pontos[1]
    pt_t2 = pontos[1] + pontos[0]
    
    return {t2:pt_t2,t1:pt_t1}
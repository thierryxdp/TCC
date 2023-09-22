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
    
    pt_jogo1 = ([gols_1_1, gols_2_1])
    pt_jogo2 = ([gols_1_2, gols_2_2])
    
    pt_t1 = pt_jogo1[0] + pt_jogo2[1]
    pt_t2 = pt_jogo1[1] + pt_jogo2[0]
    
    if pt_t1>pt_t2:
        pontos1=6 and pontos2=0
    if pt_t1==pt_t2:
        pontos1=2 and pontos2=2
   	if pt_t1<pt_t2:
        pontos1=0 and pontos2=6
    
    return {t2:pontos2,t1:pontos1}
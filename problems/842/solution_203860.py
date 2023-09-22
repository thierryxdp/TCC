def pontos_por_time(x):
    jg1 = x[0]
    jg2= x[1]
    
    t1 = x[0][0]
    t2 = x[0][1]
    
    gols_1_1 = jg1[2][0]
    gols_2_1 = jg1[2][1]
    gols_1_2 = jg2[2][0]
    gols_2_2 = jg2[2][1]
    
    if gols_1_1<gols_2_1 and gols_1_2<gols_2_2:
        pontos1=6 and pontos2=0
    
    return{t2:pontos2,t1:pontos1}
               
    
    
   
    
	return {t2:pt_t2,t1:pt_t1}
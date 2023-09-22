def pontos_por_time(time1,time2,pontos1,timev1,timev2,pontosv1):
    
    jogo1={time1:pontos1[0],
           time2:pontos1[1],
           pontos1[0]:plac1,
           pontos1[1]:plac2}
    jogo2={timev1:pontosv1[1],
           timev2:pontosv1[0],
           pontosv1[0]:plac1,
           pontosv1[1]:plac2}
    if pontos1[0]>pontos1[1]:
        plac1=plac1+3
        
    elif pontos1[0]==pontos1[1]:
    	plac1=plac1+1
        
    if pontos1[1]>pontos1[0]:
        plac2=plac2+3
        
    elif pontos1[1]==pontos1[0]:
    	plac2=plac2+1
        
    if pontosv1[0]>pontosv1[1]:
        plac2=plac2+3
        
    elif pontosv1[0]==pontosv1[1]:
    	plac2=plac2+1
        
    if pontosv1[1]>pontosv1[0]:
        plac1=plac1+3
        
    elif pontosv1[1]==pontosv1[0]:
    	plac1=plac1+1
        
    return str(time1)+" "+jogo1[pontos1[0]]+" "+str(time2)+" "+jogo[pontos[1]]
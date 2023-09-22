def pontos_por_time([[time1,time2,[x1,x2]],[time2,time1,[y2,y1]]]):
    if x1>x2:
       jogo1t1=3 
    elif x2>x1:
         jogo1t2=3 
    elif x1=x2:
         jogo1t1=jogo1t2=1
    elif x1<x2:
         jogo1t1=0
    elif x2<x1:
         jogo1t2=0
    elif y2>y1:
         jogo2t2=3            
    elif y1>y2:                 
         jogo2t1=3
    elif y2=y1:
         jogo2to=jogo2t1=1
    elif y2<y1:
         jogo2t2=0
    elif y1<y2:
         jogo2t1=0            
         return: {time1:jogo1t1+jogo2t1,time2:jogo1t2+jogo2t2}
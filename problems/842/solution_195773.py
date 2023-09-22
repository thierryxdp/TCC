def pontos_por_time[[time1,time2,[x,y]],[time2,time1,[t,r]]]:
    ptime1=[]
    ptime2=[]
    if x==y :
        ptime1= ptime1 + 1
        ptime2= ptime2 + 1
    if x>y:
        ptime1=ptime1+ 3
    if y>x:
        ptime2= ptime2 +3
    if t==r:
        ptime1= ptime1 + 1
        ptime2= ptime2 + 1
    if t>r:
        ptime2= ptime2+ 3
    if r>t:
        ptime1=ptime1+3
        
    return {time1: ptime1, time2:ptime2}
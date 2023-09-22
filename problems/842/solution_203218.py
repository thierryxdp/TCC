""" pontos_por_time(['Bots','Flafla',[2,0]],['Flafla','Bots',[2,0]])
    pontos_por_time(['Bots','Flafla',[2,0]])"""
def pontos_por_time(time1,time2):
    t1=time1[0]
    t2=time1[1]
    #agora as coisas se invertem
    tv1=time2[0]
    tv2=time2[1]
    #time1[2][0] é o do bots, time1[2][1] é o do flafla
    #time2[2][0] é o do flafla, time2[2][1] é o do bots
    pt1=time1[2][0]+time2[2][1]
    pt2=time1[2][1]+time2[2][0]
    if pt1>pt2:
        pt1=pt1+3
        
    elif pt1==pt2:
        pt1=pt1+1
        
    if pt2>pt1:
        pt2=pt2+3
        
    elif pt2==pt1:
        pt2=pt2+1
        
    return {t2+" "+str(pt1)+" "+t1+" "+str(pt2)}
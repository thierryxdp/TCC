#Start your python function here
def pontos_por_time(time1,time2,pontos1,pontosv1):
    plac1=0
    plac2=0
    if pontos1[0]>pontos1[1]:
        plac1=plac1+3
        
    elif pontos1[0]==pontos1[1]
    	plac1=plac1+1
        
    if pontos1[1]>pontos1[0]:
        plac2=plac2+3
        
    elif pontos1[1]==pontos1[0]
    	plac2=plac2+1
        
    if pontosv1[0]>pontosv1[1]:
        plac2=plac2+3
        
    elif pontosv1[0]==pontosv1[1]
    	plac2=plac2+1
        
    if pontosv1[1]>pontosv1[0]:
        plac1=plac1+3
        
    elif pontosv1[1]==pontosv1[0]
    	plac1=plac1+1
    lista={time1:plac1,
           time2:plac2}
    return str(time1)+" "+lista[time1]+" "+str(time2)+" "+lista[time2]
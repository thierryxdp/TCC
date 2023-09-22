def pontos_por_time(lista):
    time1=0
    time2=0
    pontos = {'Cormengo', 'Flamínthians':[time1,time2],'Flamínthians','Cormengo':[time1,time2]}
    
    if pontos[0][2][0]>pontos[0][2][1]:
        time1=time1+3
    elif pontos[0][2][0]<pontos[0][2][1]:
        time2=time2+3
    else:
        time1=time1+1
        time2+time2+1
    if pontos[1][2][0]>pontos[1][2][1]:
        time1=time1+3
    elif pontos[1][2][0]<pontos[1][2][1]:
        time2=time2+3
    else:
        time1=time1+1
        time2=time2+1
         
   return pontos
def pontos_por_time(L):
    time1=0
    time2=0
    
    if jogoi[0][2][0]>jogoi[0][2][1]:
        time1=time1+3
    elif jogoi[0][2][0]>jogoi[0][2][1]:
        time2=time2+3
    else:
        time1=time1+1
        time2+time2+1
    if jogov[1][2][0]>jogov[1][2][1]:
        time1=time1+3
    elif jogov[1][2][0]<jogov[1][2][1]:
        time2=time2+3
    else:
        time1=time1+1
        time2=time2+1
         
  return {nome_t1,nome_t2:time1,time2, nome_t2,nome_t1:time2, time1}
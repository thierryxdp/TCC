#Start your python function here
def pontos_por_time(lista):
    pontos_Time = {}
    pontosTime1 = 0
    pontosTime2 = 0
      
    placar1 = lista[0][2]
    if placar1[0]>placar1[1]:
        pontosTime1 = pontosTime1 + 3
    elif placar1[0]<placar1[1]:
        pontosTime2 = pontosTime2 + 3
    else:
        pontosTime1 = pontosTime1 + 1
        pontosTime2 = pontosTime2 + 1
        
    placar2 = lista[1][2]
    if placar2[0]>placar2[1]:
        pontosTime2 = pontosTime2 + 3
    elif placar2[0]<placar2[1]:
        pontosTime1 = pontosTime1 + 3
    else:
        pontosTime1 = pontosTime1 + 1
        pontosTime2 = pontosTime2 + 1
  
    pontos_Time[lista[0][0]] = pontosTime1
    pontos_Time[lista[0][1]] = pontosTime2
    
    return pontos_Time
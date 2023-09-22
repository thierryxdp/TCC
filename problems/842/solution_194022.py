def pontos_por_time(lista):

 j1t1= lista[0][2][0]

 j1t2 = lista[0][2][1]

 j2t1= lista[1][2][1]

 j2t2 = lista[1][2][0]

 time1=lista[0][0]

 time2=lista[0][1]

 if j1t1 > j1t2 and j2t1 > j2t2:

  return {time1 : 6, time2 : 0}
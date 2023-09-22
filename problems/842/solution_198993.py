#Start your python function here
def pontos_por_time(lista):
 if (lista[0][2][0]>lista[0][2][1] and lista[1][2][1]>lista[1][2][0]):
    status=6                                                              
 elif ( lista [0][2][1]>lista[0][2][0] and lista[1][2][0]>lista[1][2][1]):
    status=6
 
 elif( lista[0][2][0]==lista[0][2][1] and lista[1][2][1]<lista[1][2][0]) or (lista[0][2][0]==lista[0][2][1] and lista[1][2][1]<lista[1][2][0]):
      status=1
 elif (lista [0][2][1]==lista[0][2][0] and lista[1][2][0]<lista[1][2][1]) or (lista [0][2][1]==lista[0][2][0] and lista[1][2][0]<lista[1][2][1]):
    status=1
 elif ( lista[0][2][0]>lista[0][2][1] and lista[1][2][1]<lista[1][2][0]) or (lista[0][2][0]<lista[0][2][1] and lista[1][2][1]>lista[1][2][0]):
    status=3
 elif(lista [0][2][1]>lista[0][2][0] and lista[1][2][0]<lista[1][2][1]) or (lista [0][2][1]<lista[0][2][0] and lista[1][2][0]>lista[1][2][1]):
      status=3
 elif(lista[0][2][0]==lista[0][2][1] and lista[1][2][1]==lista[1][2][0]):
    status=2
 elif (lista [0][2][1]==lista[0][2][0] and lista[1][2][0]==lista[1][2][1]):
    status=2
 elif lista[0][2][0]<lista[0][2][1] and lista[0][2][0]<lista[0][2][1]:
      status=0
 elif lista [1][2][0]<lista[1][2][0] and lista[1][2][1]<lista[1][2][0]:
      status=0
 return {lista[0][0]:status, lista[0][1]:status}
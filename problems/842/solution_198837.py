#Start your python function here
def pontos_por_time(lista):
 if lista[0][2][0]>lista[0][2][1] or lista[0][2][1]>lista[0][2][0]:
     pontos=3
 elif lista[0][2][1]==lista[0][2][0]:
     pontos=1
 return {lista[0][0]:pontos }
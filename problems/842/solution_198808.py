#Start your python function here
def pontos_por_time(lista):
 if lista[0][2][0]>lista[0][2][1] or lista[0][2][1]>lista[0][2][0]:
     status=3
 elif lista[0][2][1]==lista[0][2][0]:
     status=1
 elif lista[1][2][0]>lista[1][2][1] or lista[1][2][1]>lista[1][2][0]:
      pontos=3
 elif lista[1][2][1]==lista[1][2][0]:
     pontos=2
        gabi=status+pontos
 return{lista[0][0]:gabi , lista[0][1]:gabi}
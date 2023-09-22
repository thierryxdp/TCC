def melhor_volta(matriz):
 '''Retorna uma tupla informando: de quem foi a melhor volta, com qual tempo e qual foi a volta.
 list -> tuple'''
 t = (0,float('inf'),0)
 for i in range(6):
   for j in range(10):
     if matriz[i][j] < t[1]:
       t = (i+1,matriz[i][j],j+1)
 return t
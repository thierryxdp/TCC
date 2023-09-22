def melhor_volta(matriz):
 t = (0,0)
 for i in range(6):
   for j in range(6, 10):
     if matriz_tempos[i][j] < tupla[1]:
       t = (i,matriz_tempos[i][j],j+1)
 return t
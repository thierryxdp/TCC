def melhor_volta(matriz_tempos):
    menor = 1

 for i in range(6):

   for j in range(10):

     if matriz_tempos[i][j] < menor:

       tupla = (i+1,matriz_tempos[i][j],j+1) #de quem, tempo, qual volta

 return tupla
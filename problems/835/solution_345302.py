def melhor_volta(mat):
    '''função que recebe como entrada uma matriz 6 × 10 com os tempos em segundos dos
    corredores em cada volta. A funç˜ao retorna uma tupla informando: De quem foi a melhor
    volta da prova, com qual tempo e em que volta.
    list->tuple '''
   tupla=(0,100**100,0)
   for i in range(6):
       for j in range(10):
           if(mat[i][j]<tupla[1]):
               tupla=(i+1,matriz[i][j],j+1)
   return tupla
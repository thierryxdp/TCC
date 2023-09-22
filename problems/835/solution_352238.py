def melhor_volta(tempos):
    
    '''dada uma matriz 6x10 onde 6 é o numero de corredor e 10
    o numero de tempos'''
    '''list->tupla'''

 tupla = (0,float('inf'),0)

 for i in range(6):

   for j in range(10):

     if tempos[i][j] < tupla[1]:

       tupla = (i+1,tempos[i][j],j+1)

 return tupla
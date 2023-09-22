def melhor_volta(matriz_tempos):
    """função que recebe o tempo de 6 corredores em dez voltas e 
    retorna de quem foi a melhor volta, com qual tempo e em qual volta
    list -> list"""

 lista = [0,float('inf'),0]

 for i in range(6):

   for j in range(10):

     if matriz_tempos[i][j] < lista[1]:

       lista = i+1,matriz_tempos[i][j],j+1
 return lista
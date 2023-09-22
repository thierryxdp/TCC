def melhor_volta(matriz_tempos):
    """função que informa de quem foi a melhor volta, com qual tempo e
    em que volta.
    list -> list"""

 lista = [0,float('inf'),0]

 for i in range(6):

   for j in range(10):

     if matriz_tempos[i][j] < lista[1]:

       lista = [i+1,matriz_tempos[i][j],j+1]
 return tupla
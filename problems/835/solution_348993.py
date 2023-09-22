def melhor_volta(matriz_tempos):
	"""função que recebe uma matriz com os tempos em segundos 
    dos corredores e retorna de quem foi a amelhor volta, o menor tempo
    e em qual volta. 
    list -> lista """
    
 lista = [0,float('inf'),0]

 for i in range(6):

   for j in range(10):

     if matriz_tempos[i][j] < lista[1]:

       lista = i+1,matriz_tempos[i][j],j+1
 return lista
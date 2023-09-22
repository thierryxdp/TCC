def melhor_volta(matriz_tempos):
    """Dados os tempos em segundos dos corredores, retorna 
    quem teve a melhor volta da prova; list -> tupla """
            
 	tupla = (0, float('inf'), 0)

 	for i in range(6):

   		for j in range(10):

     	if matriz_tempos[i][j] < tupla[1]:

       	tupla = (i+1, matriz_tempos[i][j], j+1)

	return tupla
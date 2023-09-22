def melhor_volta(lista):
    '''Encontra o menor valor de tempo e retorna uma tupla com a informações: de quem foi a melhor volta, tempo e a volta
       list -> tuple'''
    tupla = (0,float('inf'),0)
	for x in range(6):
   		for y in range(10):
     		if lista[x][y] < tupla[1]:
       		tupla = (i+1,lista[i][j],j+1) 
    return tupla
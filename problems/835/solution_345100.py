def melhor_volta(matriz):
    '''Função que retorna uma tupla com informações sobre qde quem é a melhor volta, comque tempo e em que volta'''
    

	tupla = (0,float,0)

	for i in range(6):
    	for j in range(10):
    		if matriz[i][j] < tupla[1]:
          		tupla = (i+1,matriz[i][j],j+1)
	return tupla
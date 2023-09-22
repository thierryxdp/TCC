def melhor_volta(matriz):
    '''Função que retorna uma tupla com informações sobre de quem 
    é a melhor volta, comque tempo e em que volta'''
    

	ResultadoEsperado = (0,100000,0)

	for i in range(0,6):
    	for j in range(0,10):
    		if matriz[i][j] < ResultadoEsperado[1]:
          		ResultadoEsperado = (i+1,matriz[i][j],j+1)
	return ResultadoEsperado
def melhor_volta(matriz):
    '''retorna de quem foi a melhor volta, 
    com qual tempo e em que volta; entrada-> matriz 6x10;
    list(mat)-> tupla'''
    menor=100
    i=0
    j=0
    for linha in matriz:
        for elem in linha:
            if elem <= menor:
                menor = elem
    for i in range(len(matriz)):
        for j in range(len(matriz[i])): 
    			if matriz[i][j] == menor:
                	tupla=(i+1, menor,j+1) 
	return tupla
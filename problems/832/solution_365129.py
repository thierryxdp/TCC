def eh_quadrada(matriz):
	"""Calcula e retorna se a variavel de entrada, matriz, eh quadrada, 
    considerando uma matriz como quadrada, quando nao tem linha nem coluna"""
    resultado= [] 
    for i in matriz:
        for j in i:
            if j==0:
            	resultado = resultado + [0]
    if list.count(resultado,0) == len(resultado):
    	return True
    else:
        return False
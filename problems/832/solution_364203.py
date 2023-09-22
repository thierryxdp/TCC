def eh_quadrada(matriz):
    
	'''Recebe uma matriz e retorna True se ela
    for quadrada e retorna False se nao for 
    quadrada
	list--> bool'''
	
    contador = 0
	if len(matriz) == 0:
	return True

	for item in matriz:
		if len(item) == len(matriz):
			contador += 1
	
    if contador == len(matriz):
		return True
	else:
		return False
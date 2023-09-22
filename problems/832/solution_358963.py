def eh_quadrada(matriz):
    for i in range(len(matriz)):
    	contlin = contlin + 1

	for j in range(matriz):
    	contcol = contcol + 1
        
    if contlin and contcol == 0:
        return True
    else:
        return False
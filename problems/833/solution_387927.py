def conta_numero(numero, matriz):
    ''' Esta função percorre a matriz e verifica quantas vezes
    aparece um determinado número nela
	int, list--> int'''
    contador = 0
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
        	if numero == matriz[i][j]:
            	contador += 1
    return contador
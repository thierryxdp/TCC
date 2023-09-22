def media_matriz(matriz):
    '''retorna a media de todos os numeros da matriz.lista->int'''
	soma=0
	for i in range(len(matriz)):
    	for j in matriz[i]:
        	soma=soma+j
	return round(soma/(len(matriz)*len(matriz[0])),2)
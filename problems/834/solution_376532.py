def media_matriz(matriz):
	import math
    contador=0
	soma=0
	for x in range(len(matriz)):
		for y in range(len(matriz[x])):
			contador=contador+1
			soma=soma+matriz[x][y]
	media=math.round(soma/contador,2)
	return media
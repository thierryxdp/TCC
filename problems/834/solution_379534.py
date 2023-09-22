def media_matriz(matriz):
    ''' dada uma matriz de entrada,a  funcao passara por i linhas preenchidas por j colunas, e entao retornara a media dos elementos dessa matriz/ 
    matriz = int '''
    soma = 0
    elementos = len(matriz)*len(matriz[0])
    for i in matriz:
        for j in i:
            soma += j
	return round(soma/elementos,2)
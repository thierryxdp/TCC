def conta_numero(numero,matriz):
    ''' Idéia: abrir um contador , e fazer ele andar pelas linhas da matriz
     e se enquanto ele anda algum elemento for igual ao numero,
     abro o contador e somo outro.'''
    matriz = []
    ocorrencias = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            qtd = 0
        	if matriz[i] == numero:
        		qtd = qtd+1
    	list.append(ocorrencias,qtd)
    return ocorrencias
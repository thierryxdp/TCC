def conta_numero(numero,matriz):
    '''Retorna todas as ocorrencias do numero na matriz
    int,list --> int'''
    ocorrencias = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if str(numero) in str(matriz[i][j]):
                ocorrencias += 1
                
	return ocorrencias
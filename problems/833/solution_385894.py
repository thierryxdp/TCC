def conta_numero(numero,matriz):
    '''   Retorna as ocorrencias do numero na matriz
    int,list --> int         '''
    ocor = 0
    for i in range(len(matriz)):
        for z in range(len(matriz[i])):
            if str(numero) in str(matriz[i][z]):
                ocor += 1
                
	return ocor
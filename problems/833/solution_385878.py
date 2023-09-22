def conta_numero(numero,matriz):
    '''retorna a quantidade de vezes que o numero aparece na matriz
    int,list->int'''
    
    ocorrencia=0
    
    for l in range(0,(len(matriz))):
        for c in range(0,(len(matriz[l]))):
            if numero==matriz[l][c]:
                ocorrencia+= 1
            else:
                ocorrencia+=0
	return ocorrencia
def conta_numero(numero,matriz):
    '''retorna a quantidade de vezes que o numero aparece na matriz
    int,list->int'''
    
    ocorrencia=()
    
    for l in range(0,(len(matriz)-1)):
        for c in range(0,(len(matriz[l])-1)):
            if numero==c:
                ocorrencia+= 1
            else:
                ocorrencia+=0
	return len(ocorrencia)
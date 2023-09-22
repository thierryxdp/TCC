def conta_numero(numero,matriz):
    '''retorna a quantidade de vezes que o numero aparece na matriz
    int,list->int'''
    
    ocorrencia=()
    
    for l in range(0,(len(matriz)-1)):
        for c in range(len(matriz[l])):
            if numero==c:
                ocorrencia+=(c,)
                
	return len(ocorrencia)
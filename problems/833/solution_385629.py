def conta_numero(numero,matriz):
    '''retorna quantas vezes o numero de entrada aparece na matriz
    int,list->int'''
    
    ocorrencia=[]
    
    for i in range(len(matriz)):
    	for j in range(len(matriz[i])):
            if j==numero:
                ocorrencia+=[j,]
   
	return len(ocorrencia)
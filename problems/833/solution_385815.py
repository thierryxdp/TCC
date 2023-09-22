def conta_numero(numero, matriz):
    '''
    	essa função recebe um número e uma matriz e retorna a quantidade de vezes que esse
        determinado número aparece na matriz dada.
        num, list -> num
    '''
    ocorrencia = 0
    for elem in range(len(matriz)):
        for elem in range(len(matriz[0])):
        	if elem == numero:
            	ocorrencia = ocorrencia + 1
    return ocorrencia
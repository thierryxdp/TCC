def conta_numero(numero,matriz):
    #Funcao que dado um inteiro e uma matriz de inteiros, conta e retorna quantas vezes aquele número aparece na matriz
    cnt = 0
    for linha in matriz:
        for item in linha:
            if item == numero:
            	cnt+=1
	return cnt
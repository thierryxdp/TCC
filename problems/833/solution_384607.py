def conta_numero(numero,matriz):
    ''' Dado um numero inteiro e uma matriz de interios de 
    	tamanho qualquer, conta e retorna quantas vezes 
        aquele numero aparece na matriz
        int,list -> int
	'''
    contador = 0
    for i in range(len(matriz)):
        if numero in matriz[i]:
            contador += matriz.count(numero)
 		#for j in range(len(matriz[0])):
            #if numero in matriz[j]:
             #   contador += 1
	return contador
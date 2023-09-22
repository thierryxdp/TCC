def conta_numero(numero, matriz):
    '''função que dado um número e uma matriz, conta e retorna 
    a quantidade de números dentro dessa matriz;
    int, list -> int'''
    conta = 0
    for i in range(len(matriz)):
        for h in range(len(matriz[i])):
        	if numero == matriz[i][h]:
            	conta = conta + 1
    return conta
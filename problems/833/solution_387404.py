def conta_numero(numero, matriz):
    '''essa funcao varre todos os valores dentro de uma matriz
    e retorna a quantidade de vezes que um numero n aparece dentro dela
    int, list-> int'''
    c=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
        	if matriz[i][j] == numero:
            	c=c+1
    return c
def conta_numero(numero, matriz):
    '''
    função que recebe um inteiro e uma matriz de inteiros 
    e retorna a quantidade de vezes que o inteiro aparece
    na matriz
    '''
    contador = 0
    for num in range(len(matriz)):
        M = matriz[num]
        for elem in range(len(M)):
            if M[elem] == numero:
                contador = contador + 1
            else:
                contador = contador
 	return contador
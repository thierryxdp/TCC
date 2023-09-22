def conta_numero(numero, matriz):
    '''
    Conta a quantidade de vezes que u num inteiro aparece numa matriz.
    
    Entrada/Saida:
    int, list -> int
    '''
    cont = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                cont += 1
	return cont
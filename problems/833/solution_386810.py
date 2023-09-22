def conta_numero(numero,matriz):
    '''funcao que recebe um numero inteiro e uma matriz e retorna a quantidade de vezes
    que o numero aparece na matriz
    int,list->int'''
    contagem=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
    		if (matriz[i][j]==numero):
            	contagem+=1
    return contagem
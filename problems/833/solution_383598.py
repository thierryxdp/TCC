def conta_numero(numero,matriz):
    '''função que dado um número inteiro e uma matriz de inteiros de 
    	tamanho qualquer, conta e retorna quantas vezes aquele número aparece
        na matriz. int, list->int'''
    qtd=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                qtd=qtd+1
    return qtd
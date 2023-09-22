def conta_numero(numero,matriz):
    '''retorna a recorrencia de um numero dado em uma matriz dada
    int,list->int'''
    if len(matriz)==0:
        return 0
    recorrenciatotal=0
    for i in range(len(matriz)):
        recorrencia=0
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
        		recorrencia+=1
    	recorrenciatotal+=recorrencia
    return recorrenciatotal
def conta_numero(numero,matriz):
    '''funcao que retorna quantas vezes o numero
    dado na entrada se encontra dentro da matriz
    int,list->int'''
    resultado=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                resultado=resultado+1
    return resultado
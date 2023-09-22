def conta_numero(numero,matriz):
    '''Função que dado um número inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna quantas vezes aquele número aparece na matriz
    int->list'''
    C=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                list.append(C,matriz[i][j])
    return len(C)
def conta_numero (num,matriz):
    '''
        Função que recebe um numero inteiro (num) e uma
        matriz de inteiros de tamanho qualquer (matriz) e
        retorna quantas vezes num aparece na matriz;
        int,list->int
    '''
    contando=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==num:
                contando+=1
    return contando
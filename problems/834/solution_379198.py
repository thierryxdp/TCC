def media_matriz(matriz):
    '''
        Função que recebe uma matriz de inteiros não vazia
        (matriz) e retorna a media de todos os n números da
        matriz com duas casas decimais de precisão;
        list->float
    '''
    dividendo=0 #soma
    divisor=0   #quantidade
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            dividendo+=matriz[i][j]
            divisor+=1
    return round(dividendo/divisor, 2)
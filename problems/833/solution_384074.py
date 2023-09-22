def conta_numero(numero,matriz):
    '''dado  um numero inteiro e uma matriz de inteiros de tamanho
    qualquer, conta e retorna quantas vezes aquele numero aparece
    na matriz  int,list--> int'''
    
    repetido=0
    
    for i in range(len(matriz)):
        for j in range( len(matriz[0])):
            if matriz[i][j] == numero :
                repetido += 1
    
    return repetido
def conta_numero(numero,matriz):
    '''dado  um numero inteiro e uma matriz de inteiros de tamanho
    qualquer, conta e retorna quantas vezes aquele numero aparece
    na matriz  int,list--> int'''
    
    repetido=0
    
    for i in len(matriz):
        for j in len(matriz[0]):
            if matriz[j][i] == numero :
                repetido += 1
    
    return repetido
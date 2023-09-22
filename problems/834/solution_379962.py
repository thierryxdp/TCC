def media_matriz(matriz):

    '''
    Função que recebe uma matriz como parâmetro e retorna
    a média dos termos da mesma.

    none -> float
    '''

    soma = 0
    lin = len(matriz)
    col = len(matriz[0])
    total_termos = lin + col
    
    for i in range(lin):
        for j in range(col):
            soma = soma + M[i][j]

    md = soma/total_termos
            
    return round(md,2)
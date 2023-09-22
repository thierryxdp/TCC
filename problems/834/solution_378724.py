def media_matriz(M):
    '''Funcao que retorna a media de todos os numeros de uma matriz
       list -> float
    '''
    soma = 0
    qnt = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            soma = soma + M[i][j]
            qnt = qnt + 1
    return round(soma/qnt,2)
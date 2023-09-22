def melhor_volta(matriz):
    '''
    '''
    resposta= ()
    for i in range(6):
        for j in range(10):
            if matriz[i][j] in min(matriz):
                resposta = (i+1,matriz[i][j],j+1)
    return resposta
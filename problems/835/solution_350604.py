def melhor_volta(matriz):
    '''
    '''
    resposta= ()
    for i in range(6):
        for j in range(10):
            if matriz[i][j] < resposta[1]:
                resposta = (i+1,matriz[i][j],j+1)
    return tupla
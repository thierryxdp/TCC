def melhor_volta(matriz):
    '''
    '''
    resposta= ()
    lista=matriz[0]+matriz[1]+matriz[2]+matriz[3]+matriz[4]+matriz[5]
    for i in range(6):
        for j in range(10):
            if matriz[i][j] == min(lista):
                resposta = (i+1,matriz[i][j],j+1)
    return resposta
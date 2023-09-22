def eh_quadrada(matriz):
    '''retorna se a matriz e quadrada
    matriz -> boolean'''
    resposta = True
    if matriz == []:
        resposta = True
    elif len(matriz) == len(matriz[0]):
        resposta = True
    else:
        resposta = False
    return resposta
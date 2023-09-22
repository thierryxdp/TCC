def eh_quadrada(matriz):
    '''calcular e retornar uma função para identificar se
    a matriz é quadrada
    parametros:
    list-> bool''' 
    for i, linha in enumerate(matriz):
        if len(linha) != len(matriz): 
            return False
    if matriz == []:
            return True
    return True
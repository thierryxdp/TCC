def media_matriz(matriz):
    ''' funcao que recebe uma matriz de numeros inteiros e retorna sua media
    '''
    assert (len(matriz)>0) and (len(matriz[0])>0)
    soma = 0
    qt = 0
    for linha in matriz:
        for elemento in linha:
            soma= soma+ elemento
            qt = qt + 1
    return round(soma/qt,2)
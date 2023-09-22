def eh_quadrada(matriz):
    '''
    Diz se a variavel matriz e uma matriz quadrada ou nao
        Parametros:
            matriz: list
        Saida: bool
    '''
    if matriz == []:
        return True
    else:
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if len(matriz)==len(matriz[i]):
                    return True
                else:
                    return False
def eh_quadrada(matriz):
    '''Faca uma funcao booleana que identifique se uma matriz é
    quadrada. Sendo uma matriz vazia também considerada quadrada.
    list-->bool.'''
    quant_linhas = len(matriz)
    quant_colunas = int
    if matriz == []:
        quant_colunas = len(matriz)
        return True
    for i in range(quant_linhas):
        quant_colunas = len(matriz[0])
        if (quant_linhas == quant_colunas):
            return True
    if quant_linhas != quant_colunas:
        return False
def eh_quadrada(matriz):
    quant_linhas = len(matriz)
    quant_colunas = len(matriz[0])
    for i in range(quant_linhas):
        if quant_linhas == 0 and quant_colunas == 0:
            return True
        if quant_linhas == quant_colunas:
            len(matriz) == len(matriz[0])
            return True
    if quant_linhas != quant_colunas or matriz == []:
        return False
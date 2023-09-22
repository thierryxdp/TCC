def media_matriz(matriz):
    '''Esta função retorna a média aritmética dos números de uma matriz.
'''
    total = 0
    quant_num = 0
    for linha in matriz:
        for col in linha:
            total += col
            quant_num += 1
    return round((total/quant_num),2)
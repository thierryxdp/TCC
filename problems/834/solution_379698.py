def media_matriz (matriz: list)-> float:
    '''Retorna a média de todos os elementos presentes na matriz dada'''
    soma = 0
    quant = 0
    for i in range(len(matriz)):
        for t in matriz[i]:
            soma = soma + t
        quant = quant + len(matriz[i])
    return round(soma/quant, 2)
def media_matriz (matriz):
    ''' função que dada matriz, de números inteiros não vazia,
    retorna a média de todos números da matriz com até duas casas
    decimais
    list->float'''
    
    soma = 0
    divisor = 0
    
    for i in range(len(matriz)):
        for j in matriz[i]:
            soma += j
            divisor += 1
    return round (soma/divisor,2)
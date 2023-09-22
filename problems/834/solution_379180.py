def media_matriz(matriz):
    '''retorna a média de todos os números da matriz'''
    soma = 0

    for linhas in matriz:
        soma = soma + sum(linhas)

    resultado = soma/(len(matriz)*len(matriz[0]))
    return round(resultado,0.5)
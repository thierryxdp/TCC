def conta_numero(numero, matriz_inteiros):
    '''Faça uma funcao que, dado um numero inteiro e uma matriz de inteiros
    de qualquer tamanho, retorne qunatas vezes aquele numero aparece na 
    matriz. int, list-->int.'''
    quantas_vezes = 0
    for matriz in matriz_inteiros:
        for inteiro in matriz:
            if inteiro == numero:
                quantas_vezes = quantas_vezes + 1
    return quantas_vezes
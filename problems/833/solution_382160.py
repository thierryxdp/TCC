def conta_numero(numero, matriz):
    '''função que dada um numero inteiro e uma matriz ce inteiros retorna quantas vezes o numero aparece na matriz'''
    soma = 0
    for n in range(len(matriz)):
        for i in range(len(matriz[n])):
            if matriz[n][i] == numero:
                soma = soma + 1
    return soma
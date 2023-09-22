def media_matriz(matriz):
    '''ao receber uma matriz de números inteiros não vazia,
    retorna a média de todos os números. da matriz com 2
    casas decimais.
    list -> float'''
    soma = 0
    qtdNumeros = len(matriz) * len(matriz[0])
    for linha in matriz:
        for n in linha:
            soma = soma + n
    return soma / qtdNumeros
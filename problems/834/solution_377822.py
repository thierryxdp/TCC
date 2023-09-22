def media_matriz(matriz):
    '''
    Função que dada uma matriz de inteiros não vazia,retorna a média de todos os
    numeros da matriz;
    list(list) -> float
    '''
    qtd = 0
    soma = 0

    for linha in matriz:
        for elemento in linha:
            qtd = qtd + 1
            soma = soma + elemento
    return round(soma/qtd,2)
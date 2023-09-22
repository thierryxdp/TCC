def media_matriz (matriz):
    """Função que recebe uma matriz de inteiros não vazia e retorna a média de todos os números
    dessa matriz com apenas duas casas decimais.
    matriz -> float"""
    soma = 0
    numeros = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            numeros = numeros+1
            soma = soma + matriz[i][j]
    media = soma/numeros
    return round(media,2)
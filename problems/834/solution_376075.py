def media_matriz(matriz):
    soma = 0.0
    media = 0
    nota = 1
    for i in range(len(matriz)):
        soma = soma + nota
    media = soma / nota
    return media
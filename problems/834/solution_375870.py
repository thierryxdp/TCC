def media_matriz(matriz):
    """Calcula e retorna a média aritmética de todos os números contidos
    na matrtiz, com duas casas decimais de precisão.
    list -> float"""
    soma=0
    peso=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma=soma+matriz[i][j]
            peso=peso+1
    return round(soma/peso,2)
def media_matriz(matriz:List):
    soma = 0
    for linha in matriz:
        for aij in linha:
            soma += aij
    return round(soma/len(matriz)/len(matriz[1::]),2)
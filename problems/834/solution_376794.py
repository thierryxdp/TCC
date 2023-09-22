def media_matriz(matriz):
    soma = 0
    for linha in matriz:
       for elemento in linha:
           soma += elemento
    return soma/(len(matriz)*len(matriz[0]))
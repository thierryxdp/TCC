def media_matriz(matriz):
    elementos = 0
    soma = 0
    for linha in matriz:
        elementos += len(linha)
        for numero in linha:
            soma += numero
    resposta = soma / elementos
    return round(resposta, 2)
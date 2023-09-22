def media_matriz(matriz):
    "dada uma matriz, retorna a média de todos os números na matriz"
    somatorio = 0
    contagem = 0
    for linha in matriz:
        for numero in linha:
            somatorio += numero
            contagem += 1
    return round((somatorio/contagem),2)
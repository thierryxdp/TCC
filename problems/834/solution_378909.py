def media_matriz(matriz):
    soma = 0
    for linha in matriz:
        for item in linha:
            soma += item
    media = soma/(len (matriz) * len (matriz[0]))
    media_arredondada = round(media,2)
    return media_arredondada
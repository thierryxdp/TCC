def media_matriz(matriz):
    soma = 0
    divisor = 0
    for linha in matriz:
        divisor = divisor + len(linha)
        for item in linha:
            soma = soma + item
    media = soma/divisor
    return round(media,2)
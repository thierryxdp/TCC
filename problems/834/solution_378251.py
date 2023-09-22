def conta_numero(numero, matriz):
    QuantidadeVezes = 0
    soma = 0
    media = 0
    for linhas in matriz:
        for numeros in linhas:
            soma += numeros
            QuantidadeVezes += 1
    media = soma/QuantidadeVezes
    return round(media, 2)
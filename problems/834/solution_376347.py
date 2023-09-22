def media_matriz(matriz):
    """ Conta repeticoes de numero na matriz """
    soma = 0
    media = 0
    numElementos = len(matriz) * len(matriz[0])
    linha = 0
    numTotalLinhas = len(matriz)
    while (linha < numTotalLinhas):
        for i in matriz[linha]:
            soma += i
        linha += 1
    media = soma / numElementos
    return round(media, 2)
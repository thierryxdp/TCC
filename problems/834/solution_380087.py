def media_matriz(matriz):

    contagem = 0

    divisor = 0

    for matrizes in matriz:

        divisor = divisor + len(matrizes)

        for numeros in matrizes:

            contagem = contagem + numeros

    return round(contagem/divisor, 2)
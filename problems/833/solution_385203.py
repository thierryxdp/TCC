def conta_numero(numero, matriz):
    QuantidadeVezes = 0
    for linhas in matriz:
        for numeros in linhas:
            if numero == numeros:
                QuantidadeVezes += 1
    return QuantidadeVezes
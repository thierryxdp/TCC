def conta_numero(numero, matriz):
    '''Função que dada uma matriz e um número,
    retorna a quatidade deste número dentro da matriz int, list -> int'''
    QuantidadeVezes = 0
    for linhas in matriz:
        for numeros in linhas:
            if numero == numeros:
                QuantidadeVezes += 1
    return QuantidadeVezes
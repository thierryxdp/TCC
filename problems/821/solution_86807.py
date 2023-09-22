def fatorial(numero):
    """ """
    num = numero+1
    sequencia = list(range(1,num))
    indice = 0
    proximo = 1
    while proximo < len(sequencia):
        if sequencia[indice] <= 1:
            resultado = sequencia[indice] * sequencia[proximo]
            indice += 1
            proximo += 1
        if sequencia[indice] > 1:
            resultado = resultado*sequencia[proximo]
            indice += 1
            proximo += 1
    return resultado
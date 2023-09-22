def soma_h(N):
    somaH = 0
    sequencia = range(1,N+1)
    for numero in (range(1,N+1)):
        divisao = 1/numero
        somaH += divisao
        resultado = round(somaH,2)
    return resultado
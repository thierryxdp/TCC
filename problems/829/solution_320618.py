def soma_h(N):
    soma = 1
    resultado = 0
    for numero in range(2,N+1):
        soma = soma + 1/numero
        resultado = round(soma,2)
    return resultado
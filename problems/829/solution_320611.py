def soma_h(N):
    soma = 1
    for numero in range(2,N+1):
        soma = soma + N/numero
        resultado = round(soma,2)
    return resultado
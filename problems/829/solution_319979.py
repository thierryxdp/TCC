def soma_h(N):
    soma = 0
    for i in list(range(N+1)):
        soma = soma + 1/i
    return round(soma,2)
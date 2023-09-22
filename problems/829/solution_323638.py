def soma_h(N):
    soma = 1
    for i in range(2,N+1):
        soma = soma + (1/i)
    return round(soma,2)
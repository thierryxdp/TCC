def soma_h(N):
    soma = 0
    for h in range(1,N+1):
        soma = soma + 1/h
    return round(soma,2)
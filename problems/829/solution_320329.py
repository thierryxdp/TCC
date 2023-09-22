def soma_h(N):
    soma = 1
    for x in range(1, N+1):
        soma += 1 / x
    return round(soma, 2)
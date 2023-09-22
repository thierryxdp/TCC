def soma_h(N):
    soma = 0
    for x in range(1, N):
        soma += 1 + 1 / x
    return round(soma, 2)
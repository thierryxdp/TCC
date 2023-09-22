def soma_h(N):
    soma = 0
    for i in range(N):
        soma = soma + 1/(i+1)
    return round(soma, 2)
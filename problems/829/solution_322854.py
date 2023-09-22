def soma_h(n):
    soma = 0
    for N in range(1, n+1):
        H = (1/N)
        soma = soma + H
    return round(soma, 2)
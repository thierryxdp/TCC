def soma_h (n):
    soma = 0
    for e in range(1, n+1):
        soma = soma + 1/e
    return round(soma,2)
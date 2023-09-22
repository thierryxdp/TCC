def soma_h(x):
    soma = 0
    for i in range(1, x + 1):
        soma = soma + 1/i
    return round(soma,2)
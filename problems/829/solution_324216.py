def soma_h(x):
    i = 0
    soma = 0
    while x > i:
        soma = soma + 1/i
        i = i + x
    return soma
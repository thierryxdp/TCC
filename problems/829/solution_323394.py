def soma_h(n):
    soma = 1
    i = 1
    while i < n:
        soma = soma + 1/i
        i = i + 1
    return round(soma,2)
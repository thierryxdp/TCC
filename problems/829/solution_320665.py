def soma_h (n):
    soma = 0
    for i in range (1, n+1):
        inv = (1/i)
        soma += inv
    return round (soma,2)
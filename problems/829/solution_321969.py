def soma_h(n):
    soma=1
    for x in range(n):
        if x > 0:
            soma = soma + 1/x
    return soma
def soma_h(n):
    soma = 0
    for denominador in range(1,n+1):
        soma += 1.0/denominador
    return soma
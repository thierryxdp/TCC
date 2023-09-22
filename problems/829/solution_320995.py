def soma_h(n):
    soma = 0.00
    for i in range(1):
        soma = soma + 1/n + 1/(n-1) + 1/(n-2) + 1/(n-3) + 1/(n-4) + 1/(n-5)
    return soma
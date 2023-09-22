def soma_h(n):
    soma = 0.1
    for x in list(range(1,n)):
        soma = soma + (1/x)
    return round(soma, 2)
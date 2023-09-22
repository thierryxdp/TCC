def soma_h(n):
    soma = 0
    for numero in range(1,n+1):
        soma = soma + (1/numero)
    soma = round(soma, 2)
    return soma
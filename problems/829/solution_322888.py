def soma_h(n):
    soma = 0
    for elemento in range(1,n+1):
        soma = soma + 1/elemento
    return round(soma, 2)
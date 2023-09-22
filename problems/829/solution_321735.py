def soma_h(n):
    soma = 1
    for i in range(2,n+1):
        soma = soma + (1/i)
    return round(soma,2)
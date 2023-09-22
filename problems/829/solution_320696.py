def soma_h(n):
    h = 1
    soma = 0
    for contador in range(1,n+1):
        soma = soma + (1/contador)
    return round(soma,2)
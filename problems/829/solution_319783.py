def soma_h(n):
    soma = 0
    for i in list(range(1,n+1)):
        soma += 1/i
    return round(soma,2)
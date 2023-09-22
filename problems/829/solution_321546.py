def soma_h(n):
    soma = 0
    for x in range(1,n+1):
        soma = soma + 1/x
    return round(soma)
def soma_h(n)
    h=1
    for i in range(2,n):
        soma = soma + (1/i)
    z = round(soma,2)
    return z
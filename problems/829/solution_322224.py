def soma_h(n):
    soma=0
    i=1
    for valor in range(1,n+1):
        soma=soma+(1/i)
    i=i+1
    return round(soma,3)
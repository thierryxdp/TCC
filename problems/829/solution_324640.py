def soma_h(n):
    soma=0
    i=1
    for x in range(1,n):
        soma=soma+(1/x)
    return round(soma,2)
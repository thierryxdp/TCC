def soma_h(n):
    soma=0
    i=1
    for valor in n:
        soma=soma+(1/i)
    i=i+1
    return round(soma,2)
def soma_h(n):
    i=1
    soma=0
    while i<=n:
        soma=soma+(1/i)
        i=i+1
    return round(soma,2)
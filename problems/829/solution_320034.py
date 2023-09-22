def soma_h(n):
    soma=0
    for a in range(1,n+1):
        soma=soma+(1/a)
        a=a+1
    return round(soma,2)
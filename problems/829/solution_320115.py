def soma_h(n):
    i=0
    soma=0.0
    for i in range(1,n+1):
        soma=soma + 1/i
    return round(soma,2)
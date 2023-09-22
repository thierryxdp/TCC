def soma_h(N):
    soma=0
    for i in range(N):
        if N!=0:
            soma=soma+(1/i+1)
    return round(soma,2)
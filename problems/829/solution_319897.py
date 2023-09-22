def soma_h(N):
    soma=0
    for i in range(N+1):
        if i==0:
            soma=soma
        else:
            soma+=1/i
    return round(soma,2)
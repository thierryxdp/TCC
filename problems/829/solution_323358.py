def soma_h(N):
    soma=1
    for i in range(N+1):
        soma=soma+((i+1)**(-1))
    return round(soma,2)
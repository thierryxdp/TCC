def soma_h(N):
    soma = 0
    for numero in range(1,N+1):
        soma = soma + 1/numero   
    return round(soma,2)
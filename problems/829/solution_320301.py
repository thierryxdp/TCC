def soma_h(N):
    proximo=1
    soma=0
    for proximo in range(1,N+1):
        soma = soma + proximo ** -1
        proximo=proximo+1
    return round(soma,2)
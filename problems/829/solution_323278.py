def soma_h(n):
    soma=0
    for i in range(1,n):
        soma+=soma+1/i
    return round(soma,2)
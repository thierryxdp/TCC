def soma_h(N):
    soma=0
    for numero in list(range(1,N)):
        res=1/numero
        soma=soma+res
    return round(soma,2)
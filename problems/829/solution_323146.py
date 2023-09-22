def soma_h(N):
    contador=0
    soma=0
    while contador<N:
        soma=soma+1/(contador+1)
        contador=contador+1
    return round (soma,2)
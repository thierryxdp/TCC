def soma_h(n):
    contador=0
    soma=0
    while contador<n:
        soma=soma+1/(contador+1)
        contador=contador+1
    return round(soma,2)
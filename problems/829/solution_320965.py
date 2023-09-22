def soma_h(n):
    soma = 0
    for numero in range(1,n+1):
        soma.append(1+(1/numero))
    return round(soma,2)
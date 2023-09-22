def soma_h(n):
    soma=0
    for i in range(1,n+1):
        elemento = 1/i
        soma+= elemento
    return round(soma,2)
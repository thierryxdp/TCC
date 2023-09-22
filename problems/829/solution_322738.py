def soma_h(n):
    soma = 1
    for i in range(1,n+1):
        soma = soma*1/i
    soma_2 = round(soma,2)
    return soma_2
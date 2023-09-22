def soma_h(num):
    soma = 0
    for numero in range(1,num+1):
        soma += 1/numero
    return round(soma,2)
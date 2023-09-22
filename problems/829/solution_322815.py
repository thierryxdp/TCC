def soma_h(num):
    soma = 1
    for numero in range(1,num+1):
        soma += 1/num
    return round(soma,2)
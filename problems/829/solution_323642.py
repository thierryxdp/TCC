def soma_h(n):
    i= 0
    soma= 0
    for x in range(n):
        soma += 1/(i+1)
        i+= 1
    return round(soma,2)
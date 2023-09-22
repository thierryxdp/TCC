def soma_h(n):
    soma=0
    i=1
    for x in range(0,n):
        soma=soma+(1/i)
        i++
    return round(soma,2)
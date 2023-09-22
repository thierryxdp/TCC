def soma_h(n):
    soma=0
    for i in range(n+1):
        if i>0:
            soma=soma+1/i
    return round(soma,2)
def qtd_divisores(numero):
    q=0
    for i in range(1,numero+1): 
        if numero % i == 0:
            q+=1
    return q
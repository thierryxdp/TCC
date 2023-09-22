def qtd_divisores(numero):
    ''' '''
    soma=0
    for i in range(1,numero+1):
        if numero % i==0:
            soma+=1
    return soma
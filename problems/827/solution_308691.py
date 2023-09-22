def qtd_divisores(numero):
    ''' '''
    soma=0
    for i in range(2,numero):
        if numero % i==0:
            soma+=1
    return soma
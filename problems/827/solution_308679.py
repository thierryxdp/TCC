def qtd_divisores(numero):
    ''' '''
    i=0
    for i in range(1,numero):
        if numero % i==0:
            i+=1
        return i
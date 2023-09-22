def qtd_divisores(numero):
    ''' '''
    i=0
    for i in range(1,numero+1):
        if numero % i==0:
        return i
        i+=1
    else:
        return i+1
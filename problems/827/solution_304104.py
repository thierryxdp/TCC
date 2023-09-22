def qtd_divisores(numero):
    '''Retorna a quantidade de divisores que um numero qualquer possui
       parameters:
       numero: numero qualquer
       int->int'''
    proximo=1
    lista=[]
    if numero < 0:
        return 0
    for proximo in range(1,numero+1):
        if numero%proximo==0:
            lista += [proximo]
            proximo += 1
    return len(lista)
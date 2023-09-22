def qtd_divisores(numero):
    '''Dado um número, a função deve retornar a quantidade de
    divisores que esse número tem;
    int->int'''
    
    divisores=0
    i=1
    for i in range(numero):
        if(numero%i==0):
            divisores=divisores+1
        i=i+1
            
    return (divisores)
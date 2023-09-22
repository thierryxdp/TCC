def qtd_divisores(numero):
    '''Dado um número, a função deve retornar a quantidade de
    divisores que esse número tem;
    int->int'''
    
    divisores=0
    
    for i in range(numero):
        if(numero%i==0):
            divisores+=1
            
    return (divisores)
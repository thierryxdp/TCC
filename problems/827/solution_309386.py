def qtd_divisores(n):
    '''Dado um número n, retorna quantos divisores tem esse número
    int->int'''
    divisores=0
    x=1
    
    for i in range(1,n):
        if n%i==0:
            divisores=divisores+1
            
    return divisores
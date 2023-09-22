def qtd_divisores(n):
    '''Dado um número n, retorna quantos divisores tem esse número
    int->int'''
    divisores=0
    
    for i in range(n):
        if n%i==0:
            divisores=divisores+1
            
    return divisores
def qtd_divisores(n): 
    ''' funcao que dado um numero, conta quantos divisores o
    numero tem.int->int'''
    divisores=0
    for count in range(1,n+1):
        if (n % count == 0):
            divisores += 1
    return divisores
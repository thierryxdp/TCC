def qtd_divisores(n):
    '''função que dado um númreo inteiro como parametro, retorna 
    a quantidade de divisores deste número
    int->int'''
    divisores=0
    for i in range(1,n+1):
        if n%i==0:
            divisores=divisores+1
    return divisores
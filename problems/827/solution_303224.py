def qtd_divisores(n):
    '''essa funcao conta a quantidade de divisores que o numero n tem
    int-->int'''
    divisores=0
    for i in range(1,n+1):
        if(n%i==0):
            divisores+=1
    return divisores
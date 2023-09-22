def qnt_divisores(n):
    '''função que calcula a quantidade de que um número tem;
    int/float -> int'''
    divisores=0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores +=1
    
    return divisores
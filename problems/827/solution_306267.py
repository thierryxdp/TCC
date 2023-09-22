def qtd_divisores (n):
    '''Dado um numero n retorna a quantidade de numeros inteiros divisores
    por ele;
    int->int'''
    divisivel=0
    for x in range (1,n+1):
        if n % x ==0:
            divisivel+=1
    return divisivel